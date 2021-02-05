import copy


class MovimentsLocalSearch:

    '''
    Método troca as posições i e j
    '''

    def swap(self, solution, i, j):
        aux = solution[i]
        solution[i] = solution[j]
        solution[j] = aux
        return solution

    '''
    Método troca i,x e y por j,z e k, sendo
    x, i+1 e y, i+2
    z, j+1 e k, j+2
    '''

    def replaceIXYandJZK(self, solution, i, j):
        size = len(solution)
        x = i+1
        y = i+2
        z = j+1
        k = j+2
        if i == size - 1:
            x = 0
            y = 1
        if j == size - 1:
            z = 0
            k = 1
        if x == size - 1:
            y = 0
        if z == size - 1:
            k = 0

        if x != j and y != j and x != z and y != k and x != k and y != z and z != i and k != i:
            auxJ = solution[j]
            auxI = solution[i]
            auxX = solution[x]
            auxY = solution[y]
            auxZ = solution[z]
            auxK = solution[k]

            solution[i] = auxJ
            solution[j] = auxI
            solution[x] = auxZ
            solution[y] = auxK
            solution[z] = auxX
            solution[k] = auxY
        return solution

    '''
    Método troca i,x e y por k,z e j, sendo
    x, i+1 e y, i+2
    z, j+1 e k, j+2
    '''

    def replaceIXYandKZJ(self, solution, i, j):
        x = i+1
        y = i+2
        z = j+1
        k = j+2
        size = len(solution)
        if i == size - 1:
            x = 0
            y = 1
        if j == size - 1:
            z = 0
            k = 1
        if x == size - 1:
            y = 0
        if z == size - 1:
            k = 0

        if x != j and y != j and x != z and y != k and x != k and y != z and z != i and k != i:
            auxJ = solution[j]
            auxI = solution[i]
            auxX = solution[x]
            auxY = solution[y]
            auxZ = solution[z]
            auxK = solution[k]

            solution[i] = auxK
            solution[j] = auxY
            solution[x] = auxZ
            solution[y] = auxJ
            solution[z] = auxX
            solution[k] = auxI
        return solution

    '''
    Método insere i após j
    '''

    def insertIafterJ(self, solution, i, j):
        # solution1 = copy.deepcopy(solution)
        cstI = solution.pop(i)
        if i < j:
            j -= 1
        solution.insert(j+1, cstI)
        return solution

    '''
    Método insere i,x após v, sendo x primeiro vizinho consecutivo de i  
    '''

    def insertIXafterJ(self, solution, i, j):
        # print(solution)
        # print("i"+str(i))
        # print("j"+str(j))
        x = i+1
        if i+1 > len(solution)-1:
            x = 0
        if x != j:
            if x > 0:
                idJ = j-2
                if i > j:
                    idJ = j
                cstI = solution.pop(i)
                cstX = solution.pop(i)
            else:
                idJ = j-1
                cstI = solution.pop(i)
                cstX = solution.pop(x)
            solution.insert(idJ+1, cstI)
            solution.insert(idJ+2, cstX)
        return solution
