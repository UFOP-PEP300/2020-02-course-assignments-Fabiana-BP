import math


class Distances:
    def __init__(self):
        self._distancesMatrix = []

    '''
    Método calcula distância euclidiana entre dois pontos cartezianos (x1,y1) e (x2,y2)
    @return distância
    '''

    def euclidianDistance(self, x1, y1, x2, y2):     
        return int(round(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))))

    def allDistances(self, customers):
        # print(len(customers))
        for i,c1 in enumerate(customers.values()):
            self._distancesMatrix.append([])
            for c2 in customers.values():
                dist = 0
                if c1 != c2:
                    dist = self.euclidianDistance(
                        c1.get_xCoord(), c1.get_yCoord(), c2.get_xCoord(), c2.get_yCoord())
                self._distancesMatrix[i].append(dist)


    def get_distancesMatrix(self):
        return self._distancesMatrix
    
    def calculeCost(self,solution):
        cost = 0
        for i in range(len(solution) - 1):
            cost += self._distancesMatrix[solution[i].get_id()-1][solution[i+1].get_id()-1]
        
        # custo do último até o primeiro
        cost += self._distancesMatrix[solution[len(solution)-1].get_id()-1][solution[0].get_id()-1]
        
        return cost
