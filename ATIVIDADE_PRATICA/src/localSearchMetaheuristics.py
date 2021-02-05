import time
import copy
import math
import numpy as np
from constructionSolution import ConstructionSolution as cs
from localSearchHeuristics import LocalSearchHeuristics as ls
from movimentsLocalSearch import MovimentsLocalSearch as mov


class LocalSearchMetaheuristics:
    def __init__(self):
        self._cs = cs()

    def grasp(self, customers, d, timeMax, itLS):
        timeIni = time.time()
        bestSolution = None
        bestCost = math.inf
        timeC = 0

        while timeC < timeMax:
            alpha = np.random.random_sample()
            solution = self._cs.cheapestInsert(customers, d, alpha)
            solution, cost = self.localSearchRandom(
                solution, d, itLS, timeIni, timeMax)

            if cost < bestCost:
                bestSolution = copy.deepcopy(solution)
                bestCost = cost

            timeC = time.time() - timeIni
        # print(timeC)

        return bestSolution, bestCost

    '''
    @param customers
    @param d
    @param timeMax tempo máximo de execução
    @param itLS número de iterações na busca local
    @param alpha razão de esfriamento geométrico
    @param SAmax número máximo de iterações em uma dada temperatura
    @param t0 temperatura inicial
    '''

    def simulatedAnnealing(self, customers, d, timeMax, itLS, alpha, SAmax, t0):
        timeIni = time.time()
        solution = self._cs.randomSolution(customers)
        cost = d.calculeCost(solution)
        bestSolution = None
        bestCost = math.inf
        timeC = 0
        temp = t0
        i = 0
        while timeC < timeMax and temp > 0.01:
            while i < SAmax:
                # gera um vizinho
                solution1, cost1 = self.localSearchRandom(
                    copy.deepcopy(solution), d, itLS, timeIni, timeMax)
                delta = cost1 - cost
                if delta < 0:
                    solution = copy.deepcopy(solution1)
                    cost = cost1
                    if cost1 < bestCost:
                        bestSolution = copy.deepcopy(solution1)
                        bestCost = cost1
                else:
                    if np.random.random_sample() < math.exp(-delta/temp):
                        solution = copy.deepcopy(solution1)
                        cost = cost1
                timeC = time.time() - timeIni
                if timeC >= timeMax:
                    break
            temp = alpha * temp
            i = 0
            timeC = time.time() - timeIni
        solution = copy.deepcopy(bestSolution)
        cost = bestCost
        # print(timeC)
        return bestSolution, bestCost

    def ils(self, customers, d, timeMax, itLS):
        timeIni = time.time()
        timeC = 0
        nivel = 2
        solution = self._cs.randomSolution(customers)
        solution, cost = self.localSearchRandom(solution, d, itLS)

        while timeC < timeMax:
            solution1 = self.pertubation(copy.deepcopy(solution), d, nivel)
            solution1, cost1 = self.localSearchRandom(
                solution1, d, itLS, timeIni, timeMax)
            if cost1 < cost or nivel > 5:
                solution = copy.deepcopy(solution1)
                cost = cost1
                nivel = 2
            else:
                nivel += 1

            timeC = time.time() - timeIni
        # print(timeC)
        return solution, cost

    def vns(self, customers, d, timeMax, itLS, nNeighborhood):
        timeIni = time.time()
        timeC = 0
        solution = self._cs.randomSolution(customers)
        cost = d.calculeCost(solution)
        while timeC < timeMax:
            k = 1
            while k <= nNeighborhood:
                # gera um vizinho de solution
                solution1, cost1 = self.localSearchRandom(
                    copy.deepcopy(solution), d, itLS)
                solution1, cost1 = self.vnd(
                    solution1, d, itLS, nNeighborhood, timeIni, timeMax)
                if cost1 < cost:
                    solution = copy.deepcopy(solution1)
                    cost = cost1
                    k = 1
                else:
                    k += 1
                timeC = time.time() - timeIni
                if timeC >= timeMax:
                    break
            timeC = time.time() - timeIni
        # print(timeC)
        return solution, cost

    def vnd(self, solution, d, itLS, nNeighborhood, timeIni=0, timeMax=math.inf):
        k = 1
        cost = d.calculeCost(solution)
        timeC = 0
        while k <= nNeighborhood and timeC < timeMax:
            # encontre o melhor vizinho de solution
            solution1, cost1 = self.localSearchBest(
                copy.deepcopy(solution), d, itLS)
            if cost1 < cost:
                solution = copy.deepcopy(solution1)
                cost = cost1
                k = 1
            else:
                k += 1
            timeC = time.time() - timeIni
        return solution, cost

    '''
    Random improvement
    '''

    def localSearchRandom(self, solution, d, maxIt, timeIni=0, timeMax=math.inf):
        M = mov()
        movs = [M.insertIafterJ, M.insertIXafterJ, M.swap,
                M.replaceIXYandJZK, M.replaceIXYandKZJ]
        cost = d.calculeCost(solution)
        it = 0
        timeC = 0
        while it < maxIt and timeC < timeMax:
            it += 1
            mv = int(np.random.randint(len(movs)))
            pos = np.random.choice(len(solution), 2, replace=False)
            solution1 = movs[mv](copy.deepcopy(solution), pos[0], pos[1])
            cost1 = d.calculeCost(solution1)
            if cost1 < cost:
                solution = copy.deepcopy(solution1)
                cost = cost1
                it = 0

            timeC = time.time() - timeIni

        return solution, cost

    '''
    Best improvement
    '''

    def localSearchBest(self, solution, d, maxIt, timeIni=0, timeMax=math.inf):
        M = mov()
        movs = [M.insertIafterJ, M.insertIXafterJ, M.swap,
                M.replaceIXYandKZJ, M.replaceIXYandJZK]
        size = len(solution)
        cost = d.calculeCost(solution)
        improvement = True
        timeC = 0

        while improvement and timeC < timeMax:  # ótimo local
            improvement = False
            bestCost = cost
            bestI = -1
            bestJ = -1
            for m in movs:
                for i in range(size-1):
                    for j in range(i+1, size):
                        solution1 = m(copy.deepcopy(solution), i, j)
                        cost1 = d.calculeCost(solution1)
                        if cost1 < bestCost:
                            bestCost = cost1
                            improvement = True
                            bestI = i
                            bestJ = j

                if improvement:
                    solution = m(solution, bestI, bestJ)
                    cost = bestCost

                timeC = time.time() - timeIni
                if timeC >= timeMax:
                    break
            timeC = time.time() - timeIni
        return solution, cost

    def pertubation(self, solution, d, nivel):
        M = mov()
        movs = [M.insertIafterJ, M.insertIXafterJ, M.swap,
                M.replaceIXYandJZK, M.replaceIXYandKZJ]

        for i in range(nivel):
            mv = int(np.random.randint(len(movs)))
            pos = np.random.choice(len(solution), 2, replace=False)
            solution = movs[mv](solution, pos[0], pos[1])
        return solution
