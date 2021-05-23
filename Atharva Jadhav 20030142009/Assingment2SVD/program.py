import numpy as np
from numpy.linalg import norm
from random import normalvariate
from math import sqrt


def getRandomUnitVector(n):
    nonNormalized = [normalvariate(0, 1) for i in range(n)]
    normalized = sqrt(sum(value * value for value in nonNormalized))
    return [value / normalized for value in nonNormalized]


def svdOneDimension(A, epsilon=1e-10):
    ''' The one-dimensional SVD '''

    n, m = A.shape
    randomUnitVector = getRandomUnitVector(min(n,m))
    previousVector = None
    currentVector = randomUnitVector

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    count = 0
    while True:
        count += 1
        previousVector = currentVector
        currentVector = np.dot(B, previousVector)
        currentVector = currentVector / norm(currentVector)

        if abs(np.dot(currentVector, previousVector)) > 1 - epsilon:
            return currentVector


def svd(A, k=None, epsilon=1e-10):

#Factor of the given array  by Singular Value Decomposition

    A = np.array(A, dtype=float)
    n, m = A.shape
    svdValues = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixForOneDimension = A.copy()

        for singularValue, u, v in svdValues[:i]:
            matrixForOneDimension -= singularValue * np.outer(u, v)

        if n > m:
            v = svdOneDimension(matrixForOneDimension, epsilon=epsilon)  # next singular vector
            nonNormalizedValue = np.dot(A, v)
            sigma = norm(nonNormalizedValue)  # next singular value
            u = nonNormalizedValue / sigma
        else:
            u = svdOneDimension(matrixForOneDimension, epsilon=epsilon)  # next singular vector
            nonNormalizedValues = np.dot(A.T, u)
            sigma = norm(nonNormalizedValues)  # next singular value
            v = nonNormalizedValues / sigma

        svdValues.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdValues)]
    print("U : ",us)
    print("\nV : ",vs)
    print("\nS : ",singularValues)
    return singularValues, us.T, vs

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


if __name__ == "__main__":
    inputArray = np.array([
        [2, 2, 4],
        [4, 5, 7],
        [2, 8, 1]])
    v = svdOneDimension(inputArray)
    output = svd(inputArray)
    
    print("\nFrom the input file-------------------\n")
    inputFromFile = getInputFromFile("input.txt")
    inputArray = np.array(inputFromFile)
    v = svdOneDimension(inputArray)
    output = svd(inputArray)
