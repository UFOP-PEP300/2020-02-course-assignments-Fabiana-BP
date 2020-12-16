from instancesReading import InstancesReading as ir
from distances import Distances as dist
import menu
import sys

def main():
    # nomes dos arquivos recebidos por parâmetros
    args  = sys.argv
    if len(args)>1:
        f = args[1] # primeiro parâmetro é o nome do sistema
        datas = ir(f)
        customers = datas.readFile()
        d = dist()
        d.allDistances(customers)
        menu.menu(customers,d)
        
    
    while True:
        f = input('Insira o caminho do arquivo ou q para sair da aplicação:\n')
        if param == 'q':
            exit(1)
        datas = ir(f)
        customers = datas.readFile() # dicionário
        d = dist()
        d.allDistances(customers)
        menu.menu(customers,d)        



if __name__ == "__main__":
    main()

