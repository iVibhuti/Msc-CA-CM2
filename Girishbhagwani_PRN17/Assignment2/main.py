import numpy as np
from numpy.linalg import norm
from random import normalvariate
from math import sqrt


def func_1(n):
    imaginative = [normalvariate(0, 1) for _ in range(n)]
    theNorm = sqrt(sum(x * x for x in imaginative))
    return [x / theNorm for x in imaginative]


def func_2(A, epsilon=1e-10):
    

    n, m = A.shape
    x = func_1(min(n,m))
    lastV = None
    currentV = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        lastV = currentV
        currentV = np.dot(B, lastV)
        currentV = currentV / norm(currentV)

        if abs(np.dot(currentV, lastV)) > 1 - epsilon:
            return currentV


def svd(A, k=None, epsilon=1e-10):
   
#Factor of the given array  by Singular Value Decomposition
  
    A = np.array(A, dtype=float)
    n, m = A.shape
    svdSoFar = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()

        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        if n > m:
            v = func_2(matrixFor1D, epsilon=epsilon)  # next singular vector
            u_imaginative = np.dot(A, v)
            sigma = norm(u_imaginative)  # next singular value
            u = u_imaginative / sigma
        else:
            u = func_2(matrixFor1D, epsilon=epsilon)  # next singular vector
            v_imaginative = np.dot(A.T, u)
            sigma = norm(v_imaginative)  # next singular value
            v = v_imaginative / sigma

        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    print("U : ",us)
    print("\nV : ",vs)
    print("\nS : ",singularValues)
    return singularValues, us.T, vs



if __name__ == "__main__":
    myarray = np.array([
        [1, 2, 3],
        [4, 6, 7],
        [8, 9, 1]])
    v1 = func_2(myarray)
    theSVD = svd(myarray)
