import math
#---Verificamos que sea posible insertar un valor en dicha posición
def EsSeguro(MatrizSud, Fila, Columna, Num,N):
    #---Verifica en la Fila
    for d in range(0,N):
        if(MatrizSud[Fila][d]==Num):
           return False
    #---Verificamos en la columna
    for r in range(0,N):
        if (MatrizSud[r][Columna] == Num):
            return False
    raizCu =int(math.sqrt(N))
    CuadroDeFila = int(Fila - Fila % raizCu)
    CuadroDeColumna =int(Columna - Columna % raizCu)
    #---Verificamos en cada cuadrante
    for r in range(CuadroDeFila,CuadroDeFila + raizCu):
        for d in range(CuadroDeColumna,CuadroDeColumna + raizCu):
            if (MatrizSud[r][d] == Num):
                return False
    return True
def ResolverSudoku(MatrizSud, N):
    Fila = -1
    Columna = -1
    EstaVacio = True
    for i in range(0,N):
        for j in range(0,N):
            if (MatrizSud[i][j] == 0):
                Fila = i
                Columna = j
                EstaVacio = False
                break
        if (EstaVacio!=True):
            break
    if (EstaVacio):
        return True
    for Num in range (1, N+1):
        if (EsSeguro(MatrizSud, Fila, Columna, Num,N)):
            MatrizSud[Fila][Columna] = Num
            #---Cuando no encontramos la solucion volvemos atras
            if (ResolverSudoku(MatrizSud, N)):
                return True
            else:
                MatrizSud[Fila][Columna] = 0
    return False
#   Mostrar Matriz
def Mostrar(MatrizSud, N):
    for r in range(0,N):
        S=""
        for d in range(0,N):
            S+=str(MatrizSud[r][d])+" "
        print(S)
SudokuMatriz = [[5, 3, 0, 0, 7, 0, 0, 0,0 ],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9] ]
ResolverSudoku(SudokuMatriz, 9)
Mostrar(SudokuMatriz, 9)

##Source: https://www.geeksforgeeks.org/sudoku-backtracking-7/ 
