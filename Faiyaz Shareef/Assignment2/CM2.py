
import numpy as np
from numpy.linalg import *
import cmath
import math
from sympy import *
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m","pip","install", package])


def getU(a,at):
    W=a*at
    s=shape(W)

    I=eye(s[0])*λ
    #applying W-λI
    fa=W-I


    exp=fa.det()
    roots= solve(exp, dict=False)

    U=calculateEigenVector(fa,roots)
    return U

def getV(a,at):
    sa=shape(a)
    W=at*a
    s=shape(W)
    I=eye(s[0])*λ
    fa=W-I

    exp=fa.det()
    roots= solve(exp, dict=False)
    sroots=roots
    sroots=list(filter(lambda num: num != 0, sroots))
    lmat = [[0 for c in range(sa[1])] for r in range(sa[0])]
    
    for i in range(len(sroots)):
        lmat[i][i]=math.sqrt(sroots[i])

    mat=Matrix(lmat)       
    
    V=calculateEigenVector(fa,roots)
    return V, mat

def calculateEigenVector(mt,rt):
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


def getFactorsOfSvd(a,at,n):
    mat = np.array(n)
    sa=shape(a)
    Vt=at*a
    s=shape(Vt)
    I=eye(s[0])*λ
    fa=Vt-I
    U=getU(a,at)
    V, Σ=getV(a,at)  
    du, dΣ, dv = svd(n)

    lmat = [[0 for c in range(sa[1])] for r in range(sa[0])]
    roots=dΣ.tolist()
    for i in range(len(roots)):
        lmat[i][i]=roots[i]
    dΣ = np.array(lmat)

    exp=fa.det()
    roots= solve(exp, dict=False)
    sroots=roots
    sroots=list(filter(lambda num: num != 0, sroots))
    rmat = [[0 for c in range(sa[1])] for r in range(sa[0])]
    for i in range(len(sroots)):
        rmat[i][i]=math.sqrt(sroots[i])
    U=du
    Vt=dv
    Σ=dΣ
    return U,Σ,Vt


def getSvd(mat):


    var('λ')
    a=Matrix(mat)
    at=a.T
    print("The Input Matrix:\n")
    print(a)

    U,Σ,VT= getFactorsOfSvd(a,at,mat)
    print("\nFactors of the given Matrix by Singular Value Decomposition:")
    print("\nU=", U, "\n\ns=", Σ, "\n\nV^t=", VT)
    
    print("\n The Matrix after multiplying all factors together:")

    #applying the svd formula here
    svd_form = (U @ Σ @ VT)
    print(svd_form)


def TakeInputFromFile(filename):
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
 
   matrix = TakeInputFromFile("Input_File.txt") 
  
   getSvd(matrix)
