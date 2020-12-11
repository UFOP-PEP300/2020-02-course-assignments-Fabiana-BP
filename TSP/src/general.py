from constructionSolution import ConstructionSolution as cs

class General:
    _customers = None
    _d = None

    def __init__(self,customers,d):
        self._customers = customers
        self._d = d
        self._construction = cs()
        self._population = []

    def generateSolution(self):
        print("Solução aleatória")
        solution = self._construction.randomSolution(self._customers)
        print("Custo: %d"% self._d.calculeCost(solution))
        self._population.append(solution)
        solution = self._construction.nearestNeighborhood(self._customers,self._d)
        print("Custo: %d"% self._d.calculeCost(solution))
        self._population.append(solution)

