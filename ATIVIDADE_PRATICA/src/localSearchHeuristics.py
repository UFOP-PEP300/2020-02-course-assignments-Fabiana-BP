import numpy as np
import copy
from movimentsLocalSearch import MovimentsLocalSearch as mv


class LocalSearchHeuristics:
    '''
    Método faz a busca local random improvement descent 
    critério de parada: máximo de iterações sem melhoras
    '''

    def __init__(self):
        self._mv = mv()

    def randomImprovement(self, solution, d, maxIt):
        cost = d.calculeCost(solution)
        it = 0
        while it < maxIt:
            it += 1
            pos = np.random.choice(len(solution), 2, replace=False)
            solution1 = self._mv.insertIafterJ(
                copy.deepcopy(solution), pos[0], pos[1])
            cost1 = d.calculeCost(solution1)
            if cost1 < cost:
                cost = cost1
                solution = copy.deepcopy(solution1)
                it = 0

        return solution, cost

    '''
    Método faz a busca local first improvement descent 
    critério de parada: ótimo local
    '''

    def firstImprovement(self, solution, d):
        size = len(solution)
        cost = d.calculeCost(solution)
        improvement = True
        while improvement:  # ótimo local
            improvement = False
            for i in range(size-1):
                for j in range(i+1, size):
                    solution1 = self._mv.insertIafterJ(
                        copy.deepcopy(solution), i, j)
                    cost1 = d.calculeCost(solution1)
                    if cost1 < cost:
                        cost = cost1
                        improvement = True
                        solution = copy.deepcopy(solution1)
                        break

                if improvement:
                    break

        return solution, cost

    '''
    Método faz a busca local best improvement descent 
    critério de parada: ótimo local
    '''

    def bestImprovement(self, solution, d):
        size = len(solution)
        cost = d.calculeCost(solution)
        improvement = True

        while improvement:  # ótimo local
            improvement = False
            bestCost = cost
            bestI = -1
            bestJ = -1
            for i in range(size-1):
                for j in range(i+1, size):
                    solution1 = self._mv.insertIafterJ(
                        copy.deepcopy(solution), i, j)
                    cost1 = d.calculeCost(solution1)
                    if cost1 < bestCost:
                        bestCost = cost1
                        improvement = True
                        bestI = i
                        bestJ = j

            if improvement:
                solution = self._mv.insertIafterJ(solution, bestI, bestJ)
                cost = bestCost

        return solution, cost
