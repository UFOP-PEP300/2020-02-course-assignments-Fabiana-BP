import numpy as np
import copy
import math
import numpy as np


class ConstructionSolution:

    '''
    Método gera solução aleatória
    '''

    def randomSolution(self, customers):
        csts = list(customers.values())
        solution = np.random.choice(csts, len(csts), replace=False)
        solution = solution.tolist()
        return solution

    '''
    Método gera uma solução a partir da heurística inserção mais barata
    '''

    def cheapestInsert(self, customers, d, alpha=0):
        path = []
        candidates = [* range(1, len(customers)+1)]
        # escolher três clientes iniciais
        csts = list(customers.values())
        path = np.random.choice(csts, 3, replace=False)
        path = path.tolist()

        # atualizar lista de candidatos
        for c in path:
            candidates.remove(c.get_id())
        # print(path)

        while candidates:
            candidates, path = self.findBest(customers,
                                             candidates, d, alpha, path)
            # print(path)

        # print(path)
        return path

    '''
    Método retorna o melhor cliente para ser inserido entre os clientes i e j
    '''

    def findBest(self, customers, candidates, d, alpha, path):
        auxDistances = []
        auxNodes = []
        # print(path)
        # computar distância de acrescentar c entre i e j
        for p in range(len(path) - 1):
            i = path[p].get_id()
            j = path[p+1].get_id()
            for c in candidates:
                cost = d.get_distancesMatrix(
                )[i-1][c-1] + d.get_distancesMatrix()[c-1][j-1] - d.get_distancesMatrix()[i-1][j-1]
                auxDistances.append(cost)
                auxNodes.append(("{}{}{}".format(c, i, j), [c, i, j]))
        # computar distância ao acrescentar c entre o primeiro cliente e o último
        i = path[0].get_id()
        j = path[len(path)-1].get_id()
        for c in candidates:
            cost = d.get_distancesMatrix(
            )[i-1][c-1] + d.get_distancesMatrix()[c-1][j-1] - d.get_distancesMatrix()[i-1][j-1]
            auxDistances.append(cost)
            auxNodes.append(("{}{}{}".format(c, i, j), [c, i, j]))

        listAux = np.argsort(auxDistances)  # índices dos custos ordenados
        auxNodesDic = dict(auxNodes)
        # print("auxNodes")
        # print(auxNodes)
        # print("auxDistances")
        # print(auxDistances)

        # rclSize = min + alpha(max - min)
        smax = len(candidates)
        # tamanho lista candidatos restrita
        rclSize = int(round(1 + alpha * (smax - 1)))
        neighbors = []
        cont = 0
        keys = []
        for l in listAux:
            neighbors.append(auxNodes[l][1][0])
            keys.append(auxNodes[l][0])
            cont += 1
            if cont == rclSize:
                break
        # escolher um candidato aleatório
        if neighbors:  # mexer aqui
            # print("neighbors ")
            # print(neighbors)
            idNeighbor = 0
            if len(neighbors) > 1:
                idNeighbor = np.random.randint(0, len(neighbors)-1)
            neighbor = neighbors[idNeighbor]
            candidates.remove(neighbor)
            # verificar onde irá inserir
            # print(neighbor)
            # print(auxNodesDic[keys[idNeighbor]])

            i = auxNodesDic[keys[idNeighbor]][1]
            j = auxNodesDic[keys[idNeighbor]][2]
            # print("i "+str(i))
            # print("j "+str(j))
            # print(path)

            idI = path.index(customers[i])
            idJ = path.index(customers[j])
            # print("idI {} path[idI] {}".format(idI, path[idI]))
            if idI == 0 and idJ == len(path)-1:
                path.insert(0, customers[neighbor])
            else:
                # print("id: "+str(idI))
                path.insert(idI+1, customers[neighbor])
            return candidates, path
