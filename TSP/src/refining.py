import numpy as np

class Refining:
    '''
    Método faz a busca local random improvement descent 
    critério de parada: máximo de iterações sem melhoras
    '''
    def randomImprovement(self,solution,d, maxIt):
        cost = d.calculeCost(solution)
        it = 0
        while it < maxIt:
            it += 1
            pos = np.random.choice(len(solution),2,replace=False)
            solution = self.swap(solution,pos[0],pos[1])
            cost1 = d.calculeCost(solution)
            if cost1 < cost:
                cost = cost1
                it = 0
            else:
                #desfaz movimento
                solution = self.swap(solution,pos[0],pos[1])
        
        return solution,cost

    '''
    Método faz a busca local first improvement descent 
    critério de parada: ótimo local
    '''
    def firstImprovement(self,solution,d):
        size = len(solution)
        cost = d.calculeCost(solution)
        improvement = True
        while improvement: #ótimo local
            improvement = False
            for i in range(size-1):
                for j in range(i+1,size):
                    solution = self.swap(solution,i,j)
                    cost1 = d.calculeCost(solution)
                    if cost1 < cost:
                        cost = cost1
                        improvement = True
                        break
                    else:
                        #desfaz movimento
                        solution = self.swap(solution,i,j)
                if improvement:
                    break

        return solution,cost


    '''
    Método faz a busca local best improvement descent 
    critério de parada: ótimo local
    '''
    def bestImprovement(self,solution,d):
        size = len(solution)
        cost = d.calculeCost(solution)
        improvement = True
        while improvement: #ótimo local
            improvement = False
            for i in range(size-1):
                for j in range(i+1,size):
                    solution = self.swap(solution,i,j)
                    cost1 = d.calculeCost(solution)
                    if cost1 < cost:
                        cost = cost1
                        improvement = True
                        
                    else:
                        #desfaz movimento
                        solution = self.swap(solution,i,j)

        return solution,cost

    '''
    Método troca as posições i e j
    '''
    def swap(self,solution,i,j):
        aux = solution[i]
        solution[i] = solution[j]
        solution[j] = aux
        return solution
