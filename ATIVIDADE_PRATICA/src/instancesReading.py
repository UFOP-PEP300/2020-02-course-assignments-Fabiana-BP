from customer import Customer as cst

class InstancesReading:
    def __init__(self,file):
        self._file = file
    
    def readFile(self):
        try:
            f = open(self._file,'r')
            datas = f.readlines()
            customers = []
            # 6 primeiras linhas são metadados, última EOF
            datas = datas[6:(len(datas)-1)]
            # print(datas)
            # print(datas)
            for line in datas:
                data = line.split()
                # print(data)
                try:
                    customer = cst(int(data[0]), float(data[1]), float(data[2]))
                    customers.append((customer.get_id(),customer))
                except:
                    print("Problema ao recuperar dados do arquivo.")
                    exit(1)
            return dict(customers)
        except:
            print("arquivo inválido.")
            exit(1)

    
    def readFileSolution(self,file):
        f = open(file,'r')
        datas = f.readlines()
        datas = (datas[4:(len(datas)-2)])
        # print(datas)
        datas = [int(x.split()[0]) for x in datas] 

        return datas
        
