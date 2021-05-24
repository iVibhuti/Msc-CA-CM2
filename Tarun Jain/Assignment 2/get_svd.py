import numpy as np

from numpy.linalg import *

from random import normalvariate
from math import sqrt



def getRandomUnitVector(n):
    unnormalized = [normalvariate(0, 1) for i in range(n)]
    normalized = sqrt(sum(value * value for value in unnormalized))
    return [value / normalized for value in unnormalized]


def svdOneDimension(A, epsilon=1e-10):
    ''' The one-dimensional SVD '''

    n, m = A.shape
    ruv = getRandomUnitVector(min(n,m))
    puv = None
    cv = ruv

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    count = 0
    while True:
        count += 1
        puv = cv
        cv = np.dot(B, puv)
        cv = cv / norm(cv)

        if abs(np.dot(cv, puv)) > 1 - epsilon:
            return cv


def getSvd(A, k=None, epsilon=1e-10):

#Factor of the given array  by Singular Value Decomposition

    A = np.array(A, dtype='float64')
    n, m = A.shape
    svdValues = []
    if k is None:
        k = min(n, m)
    du, dΣ, dV = svd(A)
    for i in range(k):
        matrixForOneDimension = A.copy()

        for singularValue, u, v in svdValues[:i]:
            matrixForOneDimension -= singularValue * np.outer(u, v)

        if n > m:
            v = svdOneDimension(matrixForOneDimension, epsilon=epsilon)  # next singular vector
            unnormalizedValue = np.dot(A, v)
            sigma = norm(unnormalizedValue)  # next singular value
            u = unnormalizedValue / sigma
        else:
            u = svdOneDimension(matrixForOneDimension, epsilon=epsilon)  # next singular vector
            unnormalizedValues = np.dot(A.T, u)
            sigma = norm(unnormalizedValues)  # next singular value
            v = unnormalizedValues / sigma

        svdValues.append((sigma, u, v))


    s, us, vs = [np.array(x) for x in zip(*svdValues)]

    #Create matrix for singular Values
    lmat = [[0 for c in range(m)] for r in range(n)]
    roots=dΣ.tolist()
    for i in range(len(roots)):
        lmat[i][i]=roots[i]
    dΣ = np.array(lmat)

    print("\nFactor  by SVD:")
    print("\nU=", du, "\n\ns=", dΣ, "\n\nV=", dV)

    print("\nMatrix after multiplication of all factors:")
    A_remake = (du @ dΣ @ dV)
    print(A_remake)

    return s, us, vs

# Reads the file and creates matrix based on the data inside file
def getMatrixInput(filename):
    with open(filename, "r") as data:
        elements = data.readlines()
    mat = []
    for value in elements:
        value = value.strip()
        value = value.split(',')
        value = [float(x) for x in value]
        mat.append(value[:])
    return mat


if __name__ == "__main__":

    print("Original matrix:")
    matrixinput = getMatrixInput("input.txt")
    mat = np.array(matrixinput)
    print(mat)
    getSvd(mat)
