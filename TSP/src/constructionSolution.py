import numpy as np
import copy
import math

class ConstructionSolution:

    '''
    Método gera solução aleatória
    '''
    def randomSolution(self, customers):
        csts = list(customers.values())
        solution = np.random.choice(csts,len(csts),replace=False)
        solution = solution.tolist()
        return solution

     
    '''
    Método gera solução a partir da heurística do vizinho mais próximo
    '''
    def nearestNeighborhood(self,customers,d,alpha=0):
        firstNode = np.random.choice(list(customers.values()),1)[0]
        path = []
        availableCsts = [* range(1,len(customers)+1)]
        path.append(firstNode)
        # print(firstNode)
        availableCsts.remove(firstNode.get_id())
        idCurrentCst = firstNode.get_id()
        lenght = len(availableCsts)
        for i in range(lenght):
            if alpha == 0:
                nextCst,availableCsts = self.findNeighbor(idCurrentCst,availableCsts,d)
            else:
                nextCst,availableCsts = self.findNeighbors(idCurrentCst,availableCsts,d,alpha)
            if nextCst is not None:
                path.append(customers[nextCst])
                idCurrentCst = nextCst
        return path

    '''
    Método encontra vizinho mais próximo
    '''
    def findNeighbor(self,idCurrentCst,availableCsts,d):
        cNeighborsDistances = d.get_distancesMatrix()[idCurrentCst-1]
        minD =  math.inf
        idM = -1
        for i,dist in enumerate(cNeighborsDistances):
            if (i+1) in availableCsts: #cliente ainda não visitado
                if dist < minD: #mais próximo
                    idM = i+1
        
        if idM > -1:
            nextCst = idM
            availableCsts.remove(idM)
            return nextCst, availableCsts

        return None
    
    '''
    Método encontra vizinho mais próximo conforme alpha
    '''
    def findNeighbors(self,idCurrentCst,availableCsts,d,alpha):
        cNeighborsDistances = d.get_distancesMatrix()[idCurrentCst-1]
        listAux = np.argsort(cNeighborsDistances) # ordena e retorna os índices
        
        # rclSize = min + alpha(max - min)
        smax =len(availableCsts) 
        rclSize = int(round(1 + alpha * (smax - 1))) #tamanho lista candidatos restrita
        neighbors = []
        cont = 0
        for i in listAux:
            if (i+1) in availableCsts:
                cont += 1
                neighbors.append(i+1)
                if cont == rclSize:
                    break
        # escolher um dos amigos mais próximos
        idAux = np.random.randint(0,rclSize)
        if neighbors:
            nextCst = neighbors[idAux]
            availableCsts.remove(nextCst)
            return nextCst, availableCsts

        return None