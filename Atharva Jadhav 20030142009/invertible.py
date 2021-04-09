checkerBoard = [1, -1, 1]

# find matrix of minors for first row of values
def getMatrixOfMinor(inputMatrix):
    minorMatrix = [[0 for x in range(2)], [0 for x in range(2)]]
    matrixOfMinor = []
    minorValues = []
    for j in range(3):
        for rows in range(1,3):
            for columns in range(3):
                if(columns == j):
                    continue
                minorValues.append(inputMatrix[rows][columns])
        minorMatrix[0] = minorValues[0:2]
        minorMatrix[1] = minorValues[2:4]
        minorValues = []
        matrixOfMinor.append(minorMatrix[:])
    return matrixOfMinor

# returns a determinant value of 2 by 2 matrix
def getDeterminant(input):
    determinant = (input[0][0] * input [1][1]) - (input[0][1] * input[1][0])
    return determinant

# returns the determinant of 3 by 3 matrix by calculating determinant for all the minors corresponding to 1st row
def calculateDeterminant(inputMatrix, matrixOfMinor):
    solution = 0
    for column in range(3):
        coeff = inputMatrix[0][column]
        coeff = coeff * checkerBoard[column]
        solution += coeff * getDeterminant(matrixOfMinor[column])
    return solution

# returns boolean value based on whether given determinant is singular or non-singular
def isSingular(determinant):
    print("determinant: " + str(determinant))
    if(determinant == 0):
        print("Given matrix is singular")
        return True
    else:
        print("Given matrix is non-singular")
        return False

# Reads the file and creates matrix based on the data inside file
def getInputFromFile(filename):
    with open(filename, "r") as data:
        values = data.readlines()
    valueList = []
    for value in values:
        value = value.strip()
        value = value.split(',')
        value = [float(x) for x in value]
        valueList.append(value[:])
    return valueList

# A function that takes matrix as input and returns its determinant
def callFunctions(inputMatrix):
    matrixOfMinor = getMatrixOfMinor(inputMatrix)
    determinant = calculateDeterminant(inputMatrix, matrixOfMinor)
    return determinant

#instructions
inputFromFile = getInputFromFile("input.txt")
print("MATRIX IN input.txt")
print(inputFromFile)
matrixOfMinor = getMatrixOfMinor(inputFromFile)
determinant = calculateDeterminant(inputFromFile, matrixOfMinor)
isSingular(determinant)
