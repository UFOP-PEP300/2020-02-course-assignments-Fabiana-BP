from instancesReading import InstancesReading as ir
from distances import Distances as dist
from general import General as ge
import sys

def main():
    # nomes dos arquivos recebidos por parâmetros
    args  = sys.argv
    if len(args)>1:
        args = args[1:] # primeiro parâmetro é o nome do sistema
        for param in args:
            datas = ir(param)
            customers = datas.readFile()
            d = dist()
            d.allDistances(customers)
            costs = d.get_distancesMatrix()
            # print(costs)
            # bestSolution = datas.readFileSolution("../dat/berlin52.opt.tour")
            # print(d.calculeCost(bestSolution)) # custo: 7542
            g = ge(customers,d)
            g.generateSolution()

        
    
    while True:
        param = input('Insira o caminho do arquivo ou q para sair da aplicação:\n')
        if param == 'q':
            exit(1)
        datas = ir(param)
        customers = datas.readFile() # dicionário
        d = dist()
        d.allDistances(customers)
        costs = d.get_distancesMatrix()
        # print(costs)
        g = ge(customers,d)
        g.generateSolution()
        



if __name__ == "__main__":
    main()

