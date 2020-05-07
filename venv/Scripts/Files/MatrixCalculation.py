import random

#Addition, Se suman los elementos del mismo indice. La matriz debe ser cuadrada
def addition(matriz, matriz2, row, column):
    result = []
    for i in range(len(matriz)):
        result.append([])
        for j in range(len(matriz)):
            result[i].append(0)
    for i in range(row):
        for j in range(column):
            result[i][j] = matriz[i][j] + matriz2[i][j]
    return result

#Se realiza la multiplicacion de las matrices (Fila * columna y luego se suman los resultados)
def multiplication(matriz1, matriz2, row, column):
    result = []
    for i in range(row):
        result.append([])
        for j in range(column):
            result[i].append(0)
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            # indice K (aux) me ayuda a moverme entre los indices de las matrices
            for k in range(len(matriz1[0])):
                result[i][j] += matriz1[i][k] * matriz2[k][j]
    return result

#se multiplican todos los elementos de la matrix por un solo valor
def scalar(matriz, scalarValue, row, column):
    result = []
    for i in range(row):
        result.append([])
        for j in range(column):
            result[i].append(0)
    for i in range(row):
        for j in range(column):
            result[i][j] = matriz[i][j] * scalarValue
    return result

#imprimo la matriz final
def finalresult(matriz, row, column):
    print("Now the results from ")
    for i in range(row):
        print('[ ', end='')
        for j in range(column):
            if (j < (len(matriz))-1):
                print(str(matriz[i][j]), end= ', ')
            else:
                print( str(matriz[i][j]), end=' ')
        print("]")

def finalresult2(matriz, strType, row, column):
    print("Now the results from: " + strType)
    column2 = column
    for i in range(row):
        print('[ ', end='')
        for j in range(column):
                if (j < column - 1):
                    print(str(matriz[i][j]), end=', ')
                else:
                    print(str(matriz[i][j]), end=' ')
        print("]")


def matrizInversa(matriz):
    doubleDetResult = determinante(matriz);
    det = 1 / determinante(matriz);
    nmatriz = matrizAdjunta(matriz);
    multiplicarMatriz(det, nmatriz);
    return nmatriz

#Multiplico cada elemento de la matriz por el determinante 1/determinante
#ademas, le saco el signo negativos a los ceros. (no entiendo como los ceros tienen signos negativos.)
def multiplicarMatriz(n, matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz)):
            if(matriz[i][j] == 0):
                matriz[i][j] = matriz[i][j] * -(n)
            else:
                matriz[i][j] *= n

#Para la matriz adjunta, saco los cofactores de la matriz y luego la transpongo
def matrizAdjunta(matriz):
    return matrizTranspuesta(matrizCofactores(matriz));

#obtenemos los cofactores de la matriz
def matrizCofactores(matriz):
    nm = []
    for ix in range(len(matriz)):
        nm.append([])
        for jx in range(len(matriz)):
            nm[ix].append(0)
    det = []
    for ii in range(len(matriz) - 1):
        det.append([])
        for jj in range(len(matriz) - 1):
            det[ii].append(0)
    for i in range (len(matriz)):
        for j in range (len(matriz)):
            #incializo k como Aux del indice i
            for k in range (len(matriz)):
                if (k != i):
                    # incializo L como Aux del indice j
                    for l in range (len(matriz)):
                        if (l != j):
                            if (k < i):
                                indice1 = k
                            else:
                                indice1 = k-1
                            if (l < j):
                                indice2 = l
                            else:
                                indice2 = l - 1
                            det[indice1][indice2] = matriz[k][l]
            detValor = determinante(det)
            nm[i][j] = detValor * pow(-1, i + j + 2)
    return nm

#Saco la transpusta de la matriz
def matrizTranspuesta(matriz):
    nuevam = []
    for i in range(len(matriz[0])):
        nuevam.append([])
        for j in range(len(matriz)):
            nuevam[i].append(0)
    for i in range (len(matriz[0])):
        for j in range (len(matriz)):
            nuevam[i][j] = matriz[j][i]
    return nuevam

#Funcion para obtener la determinante de una matriz
def determinante(matriz):
    if (len(matriz) == 1):
        return int(matriz[0][0])
    elif (len(matriz) == 2):
        det = (matriz[0][0] * matriz[1][1]) - (matriz[1][0] * matriz[0][1])
        return det
    elif(len(matriz) > 2):
        #inicializo la matriz que voy a ocupar, en este caso
        nm = []
        for i in range(len(matriz) -1):
            nm.append([])
            for j in range(len(matriz)-1):
                nm[i].append(0)
        suma = 0
        for i in range (len(matriz)):
            for j in range (len(matriz)):
                if (j != i):
                    for k in range (len(matriz)):
                        indice = -1
                        if j < i:
                            indice = j;
                        elif j > i:
                            indice = j - 1
                        nm[indice][k - 1] = matriz[j][k]
            if i % 2 == 0:
                suma += matriz[i][0] * determinante(nm)
            else:
                suma -= matriz[i][0] * determinante(nm)
        return suma


def RowNumber(matriz, intRowNumber):
    nm = []
    for i in range(1):
        nm.append([])
        for j in range(len(matriz)):
            nm[i].append(0)
    for i in range(1):
        for j in range(len(matriz)):
            nm[i][j] = matriz[int(intRowNumber)][j]
    return nm


def ColumnNumber(matriz, intColumnNumber):
    nm = []
    for i in range(len(matriz)):
        nm.append([])
        for j in range(1):
            nm[i].append(0)

    for i in range(len(matriz)):
        for j in range (1):
            nm[i][j] = matriz[i][int(intColumnNumber)]
    return nm

def NewMatrix(matriz, intRowDim, intColumnDim, intColumnMatrix):
    nm = []
    for i in range(int(intRowDim)):
        nm.append([])
        for j in range(int(intColumnDim)):
            nm[i].append(0)
    for i in range(int(intRowDim)):
        for j in range (int(intColumnDim)):
            try:
               nm[i][j] = matriz[i][j+int(intColumnMatrix)]
            except():
                        nm[i][k] = 0
    return nm


def CreateMatriz(row, column):
    matriz = []
    for i in range(row):
        matriz.append([])
        for j in range(column):
            matriz[i].append(0)
    for i in range(row):
        for j in range(column):
            matriz[i][j] = random.randrange(100)
    return matriz

def EntryValidation(strTypeEntry, intFlag, intData):
    while True:
        intVariable = input(strTypeEntry)
        try:
            intVariable = int(intVariable)
            if (intFlag == 0):
                if (intVariable > 0):
                    break
                else:
                    print("The number must be higher than zero")
            else:
                if (intVariable < (intData - 1) and intVariable > 0):
                    break
                else:
                    print("The number must be minor than: " + str(intData - 1))
        except ValueError:
            print("Incorrect Entry: The number must be an integer positive")
    return intVariable


intRow = EntryValidation("Insert the row matrix size: ", 0 , 0)

intColumn = EntryValidation("Insert the column matrix size: ", 0 , 0)

#matriz1 = [[0, 1, 1], [1, 0, 0], [0, 0, 1]]
# 3x3 matrix
#matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz1 = CreateMatriz(intRow, intColumn)
matriz2 = CreateMatriz(intRow, intColumn)

finalresult2(matriz1, "First Matrix.", intRow, intColumn)
finalresult2(matriz2, "Second Matrix.", intRow, intColumn)

ResultMatrixAddition = addition(matriz1, matriz2, intRow, intColumn)
finalresult2(ResultMatrixAddition, "Addition", intRow, intColumn)

ResultMatrixMultiplication = multiplication(matriz1, matriz2, intRow, intColumn)
finalresult2(ResultMatrixAddition, "Multiplication between matrix", intRow, intColumn)

intScalarMulti = EntryValidation("Insert the number to do a scalar multiplication of both matrix: ", 0 , 0)
ResultMatrixScalar = scalar(matriz1, intScalarMulti, intRow, intColumn)
finalresult2(ResultMatrixScalar, "Scalar multiplication", intRow, intColumn)
ResultMatrixScalar = scalar(matriz2, intScalarMulti, intRow, intColumn)
finalresult2(ResultMatrixScalar, "Scalar Multiplication", intRow, intColumn)

intMatrixTranspose = matrizTranspuesta(matriz1)
finalresult2(intMatrixTranspose, "Matrix 1 transpose", intColumn, intRow)
intMatrixTranspose = matrizTranspuesta(matriz2)
finalresult2(intMatrixTranspose, "Matrix 2 transpose", intColumn, intRow)

if(intRow == intColumn):
     intDeter = determinante(matriz1)
     print("The determinant is: " + str(intDeter))
     intAdjunta = matrizAdjunta (matriz1)
     finalresult2(intAdjunta, "Adjugate Matriz",len(intAdjunta), len(intAdjunta))
     if(intDeter != 0):
         invMatriz = matrizInversa(matriz1)
         finalresult2(invMatriz, "Inversed Matriz",len(invMatriz), len(invMatriz))
     else:
         print("The determinant is zero, so we can`t generate the inversed matrix")
else:
    print("The matrix isn't squared")

if( intRow>2 and intColumn >2):

    intRowNumber = EntryValidation("Insert the row number to obtain that data: ", 1, intRow)
    matrizResult = RowNumber(matriz1, intRowNumber)
    intColumn = len(matrizResult[0])
    intRow = len(matrizResult)
    finalresult2(matrizResult, "Matrix row",intRow, intColumn)

    intColumnNumber = EntryValidation("Insert the row number to obtain that data: ", 1, intColumn)
    matrizResult = ColumnNumber(matriz1, intColumnNumber)
    intColumn = len(matrizResult[0])
    intRow = len(matrizResult)
    finalresult2(matrizResult, "Column Row",intRow, intColumn)

    intRowDim = EntryValidation("Insert the new row dimensions of the new matrix from the original: ", 0,0)
    intColumnDim = EntryValidation("Insert the new column dimensions of the new matrix from the original: ", 0, 0)
    intColumnMatrix = EntryValidation("Insert from which column we are going to complete the matrix: ", 0, 0)
    matrixNewMatrix = NewMatrix(matriz1, intRowDim, intColumnDim, intColumnMatrix)
    finalresult2(matrixNewMatrix, "New Matrix",int(intRowDim), int(intColumnDim))
else:
    print("We can`t do the next operations because the matrix is less than 2x2")

