from instancesReading import InstancesReading as ir
from distances import Distances as dist
import menu
import experiment as ex
import sys


def main():
    alpha = 0.1
    itLS = 2000  # 1000, 2000, 500
    timeMax = 180
    SAmax = 1000  # 1000, 2000, 500
    nNeighborhood = 20  # 20, 50, 100
    repetitions = 10
    t0 = 1000  # 1000, 2000, 500
    # nomes dos arquivos recebidos por parâmetros
    args = sys.argv
    if len(args) > 1:
        f = args[1]  # primeiro parâmetro é o nome do sistema
        datas = ir(f)
        customers = datas.readFile()
        d = dist()
        d.allDistances(customers)
        # print(d.get_distancesMatrix())
        # menu.menu(customers, d)
        bestSolution = ex.construction(
            f, customers, d, [0.1, 0.3, 0.5], repetitions)
        ex.refiningHeuristic(f, bestSolution, d, 1000)
        ex.refiningMetaheuristics(
            f, customers, d, timeMax, itLS, alpha, SAmax, t0, nNeighborhood, repetitions)
    while True:
        f = input('Insira o caminho do arquivo ou q para sair da aplicação:\n')
        if f == 'q':
            exit(1)
        datas = ir(f)
        customers = datas.readFile()  # dicionário
        d = dist()
        d.allDistances(customers)
        # menu.menu(customers, d)
        bestSolution = ex.construction(
            f, customers, d, [0.1, 0.3, 0.5], repetitions)
        ex.refiningHeuristic(f, bestSolution, d, 1000)
        ex.refiningMetaheuristics(
            f, customers, d, timeMax, itLS, alpha, SAmax, t0, nNeighborhood, repetitions)


if __name__ == "__main__":
    main()
