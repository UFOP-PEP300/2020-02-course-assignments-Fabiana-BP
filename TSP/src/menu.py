import util
from constructionSolution import ConstructionSolution as cs
from refining import Refining as r

def menu(customers,d):
    util.mark()
    mark = 20 * "*"
    print(mark + "TSP" + mark)
    solution = []
    cost = 0

    while(True):
        mark = 20 * "*"
        print("\n1 - gerar solução")
        print("2 - calcular custo")
        print("3 - refinar solucao")
        print("q - sair\n")
        choice = input()

        if choice == "1":
            solution = menuConstruction(customers,d)
            print("solução:")
            print(solution)

        elif choice == "2":
            cost = d.calculeCost(solution)
            print("Custo: %.2f" % cost)
        elif choice == "3":
            solution,cost = menuLocalSearch(solution,d)
            print("solução:")
            print(solution)
            print("Custo: %.2f" % cost)
        elif choice == "q":
            exit(1)
        else:
            print("Comando inválido!")

def menuConstruction(customers,d):
    CS = cs()
    util.mark()
    print("1 - Solução aleatória")
    print("2 - Solução heurística do vizinho mais próximo")
    print("3 - Solução heurística do vizinho mais próximo parcialmente gulosa")
    print("q - sair")
    choice = input()
    alpha = float()
    if choice == "1":
        solution = CS.randomSolution(customers)
    elif choice == "2":
        solution = CS.nearestNeighborhood(customers,d)
    elif choice == "3":
        alpha = input("Informe o valor de alpha (0.0 a 1.0):")
        try:
            alpha = float(alpha)
            if alpha >= 0 and alpha <=1:
                solution = CS.nearestNeighborhood(customers,d,alpha)
            else:
                print("valor inválido!")
                return []
        except Exception as exc:
            print("valor inválido!")
            return []
    elif choice == "q":
        exit(1)
    else:
        print("Comando inválido!")
        return []
        

    return solution

def menuLocalSearch(solution,d):
    R = r()
    util.mark()
    print("1 - First improvement descent")
    print("2 - Best improvement descent")
    print("3 - Random descent")
    print("q - sair")
    choice = input()
    if choice == "1":
       return R.firstImprovement(solution,d)
        
    elif choice == "2":
        return R.bestImprovement(solution,d)

    elif choice == "3":
        maxIt = int()
        try:
            maxIt = input("Informe o número máximo de iterações sem melhoras:")
            maxIt = int(maxIt)
            return R.randomImprovement(solution,d,maxIt)
        except Exception as exec:
            print("Comando inválido!")
            return [],0
    elif choice == "q":
        exit(1)
    else:
        print("Comando inválido!")
        return [],0
