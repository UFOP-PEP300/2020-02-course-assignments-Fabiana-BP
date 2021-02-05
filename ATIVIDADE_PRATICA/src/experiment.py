from constructionSolution import ConstructionSolution as cs
from localSearchHeuristics import LocalSearchHeuristics as ls
from localSearchMetaheuristics import LocalSearchMetaheuristics as lsm
import math
import copy

berlin52 = 7542
kroA100 = 21282
pr124 = 59030
ch150 = 6528
kroB200 = 29437


def construction(instance, customers, d, alphas, repetitions):
    CS = cs()
    # inserção mais barata gulosa
    solution = CS.cheapestInsert(customers, d)
    cost = d.calculeCost(solution)
    print("Heurística inserção mais barata gulosa: ")
    print("Solução: ")
    print(solution)
    print("Custo: "+str(cost) + "    gap: "+str(gap(instance, cost)))
    print("\n")

    print("Heurística inserção mais barata semi gulosa: ")
    bestAllSolution = copy.deepcopy(solution)
    bestAllCost = cost
    for a in alphas:
        avgCost = 0
        bstCost = math.inf
        wstCost = 0
        worstSolution = None
        bestSolution = None
        for i in range(repetitions):
            solution = CS.cheapestInsert(customers, d, a)
            cost = d.calculeCost(solution)
            if cost < bstCost:
                bstCost = cost
                bestSolution = copy.deepcopy(solution)
            if cost > wstCost:
                wstCost = cost
                worstSolution = copy.deepcopy(solution)
            if bestAllCost > cost:
                bestAllCost = cost
                bestAllSolution = copy.deepcopy(solution)
            avgCost += cost
        avgCost /= repetitions
        print("alfa: "+str(a))
        print("Melhor solução: ")
        print(bestSolution)
        print("custo: "+str(bstCost) + "    gap: "+str(gap(instance, bstCost)))
        print()
        print("Pior solução: ")
        print(worstSolution)
        print("custo: "+str(wstCost) + "    gap: "+str(gap(instance, wstCost)))
        print()
        print("Custo médio: "+str(avgCost) +
              "    gap: "+str(gap(instance, avgCost)))
    return bestAllSolution


def refiningHeuristic(instance, solution, d, maxIt):
    LS = ls()
    bstMet = ""
    wstMet = ""
    avgCost = 0
    bstCost = math.inf
    wstCost = 0
    worstSolution = None
    bestSolution = None
    methods = [LS.firstImprovement, LS.bestImprovement]
    for m in methods:
        solution1, cost = m(copy.deepcopy(solution), d)
        if cost < bstCost:
            bstCost = cost
            bestSolution = copy.deepcopy(solution1)
            bstMet = m
        if cost > wstCost:
            wstCost = cost
            worstSolution = copy.deepcopy(solution1)
            wstMet = m
        avgCost += cost

    solution1, cost = LS.randomImprovement(copy.deepcopy(solution), d, maxIt)
    if cost < bstCost:
        bstCost = cost
        bestSolution = copy.deepcopy(solution1)
        bstMet = m
    if cost > wstCost:
        wstCost = cost
        worstSolution = copy.deepcopy(solution1)
        wstMet = m
    avgCost += cost
    avgCost /= 3

    print("Heurística de busca local: ")
    print("Melhor solução: " + str(bstMet))
    print(bestSolution)
    print("custo: "+str(bstCost) + "    gap: "+str(gap(instance, bstCost)))
    print()
    print("Pior solução: " + str(wstMet))
    print(worstSolution)
    print("custo: "+str(wstCost) + "    gap: "+str(gap(instance, wstCost)))
    print()
    print("Custo médio: "+str(avgCost) +
          "    gap: "+str(gap(instance, avgCost)))


def refiningMetaheuristics(instance, customers, d, timeMax, itLS, alpha, SAmax, t0, nNeighborhood, repetitions):
    LS = lsm()
    metas = [LS.grasp, LS.simulatedAnnealing, LS.ils, LS.vns]
    metasName = ["GRASP", "Simulated Annealing", "ILS", "VNS com VND"]
    avgCost = 0
    bstCost = math.inf
    wstCost = 0
    worstSolution = None
    bestSolution = None
    for i, m in enumerate(metas):
        avgCost = 0
        for r in range(repetitions):
            # print("repetição "+str(r))
            if i == 1:  # Simulated Annealing
                solution, cost = m(
                    customers, d, timeMax, itLS, alpha, SAmax, t0)
            elif i == 3:  # vns
                solution, cost = m(customers, d, timeMax, itLS, nNeighborhood)
            else:  # grasp ou ils
                solution, cost = m(customers, d, timeMax, itLS)
            if bstCost > cost:
                bstCost = cost
                bestSolution = copy.deepcopy(solution)
            if wstCost < cost:
                wstCost = cost
                worstSolution = copy.deepcopy(solution)
            avgCost += cost
        avgCost /= repetitions
        print("meta-heurística: " + metasName[i])
        print("Melhor solução: ")
        print(bestSolution)
        print("custo: "+str(bstCost) + "    gap: "+str(gap(instance, bstCost)))
        print()
        print("Pior solução: ")
        print(worstSolution)
        print("custo: "+str(wstCost) + "    gap: "+str(gap(instance, wstCost)))
        print()
        print("Custo médio: "+str(avgCost) +
              "    gap: "+str(gap(instance, avgCost)))


def gap(instance, cost):
    inst = instance[7:-4]
    # print("instance: "+inst)
    bestCost = 0
    if inst == 'berlin52':
        bestCost = berlin52
    elif inst == 'ch150':
        bestCost = ch150
    elif inst == 'kroA100':
        bestCost = kroA100
    elif inst == 'kroB200':
        bestCost = kroB200
    elif inst == 'pr124':
        bestCost = pr124
    else:
        return -1

    return 100*((cost - bestCost)/bestCost)
