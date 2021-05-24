
import numpy as np
import cmath
from sympy import *
import math
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#Get the U value in factors of the matrix using svd
def getU(a,at):
    W=a*at
    s=shape(W)
    I=eye(s[0])*λ
    #subtract W-Iλ
    fa=W-I
    #Get determinant of fa matrix to find Singular values
    exp=fa.det()
    roots= solve(exp, dict=False)
    #Get the eigen Vector U for fa matrix with the calculated roos
    U=getEigenVector(fa,roots)
    return U

#Get the V value in factors of the matrix using svd
def getV(a,at):
    sa=shape(a)
    W=at*a
    s=shape(W)
    #subtract W-Iλ
    I=eye(s[0])*λ
    fa=W-I
    #Get determinant of fa matrix to find Singular values
    exp=fa.det()
    roots= solve(exp, dict=False)
    sroots=roots
    sroots=list(filter(lambda num: num != 0, sroots))
     #Get the Singular Value matrix that is Sigma by calculating the root of the equation
    lmat = [[0 for c in range(sa[1])] for r in range(sa[0])]
    for i in range(len(sroots)):
        lmat[i][i]=math.sqrt(sroots[i])
    mat=Matrix(lmat)

    #Get the V for fa matrix with the calculated roots and Eigen Vector
    V=getEigenVector(fa,roots)
    return V.T,mat


def getEigenVector(mt,rt):
    l=len(rt)

    M=Matrix()
    for k in range(l):
        smt=mt.subs(λ, rt[k])
        ms= shape(smt)
        fmt=smt.nullspace()
        gmt=fmt[0]
        sp= shape(gmt)
        f = 0
        for i in range(sp[0]):
            for j in range(sp[1]):
                f=f+gmt[i,j]*gmt[i,j]
        sqt=math.sqrt(f)
        fgmt=gmt/sqt
        fgmt=fgmt.reshape(sp[0], sp[1])
        M = M.col_insert(k, gmt/sqt)
    return M

def getSvd(mat):
    #Defining Lamda as a unknown value
    var('λ')
    a=Matrix(mat)
    at=a.T
    print("Input Matrix:\n")
    print(a)

    U=getU(a,at)
    Vt, Σ=getV(a,at)

    print("\nFactors of the given Matrix by Singular Value Decomposition:")
    print("\nU=", U, "\n\ns=", Σ, "\n\nV^t=", Vt)

    #Checking if we can remake the original matrix using U,Σ,Vt
    print("\nMatrix after multiplying all factors together:")
    print(U*Σ*Vt)

 
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
    install("sympy")
    matrix = getInputFromFile("input.txt") 
    #function to print Factors
    getSvd(matrix)




