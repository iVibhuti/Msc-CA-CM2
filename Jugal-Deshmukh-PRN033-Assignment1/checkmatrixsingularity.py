'''
Python program to check whether a matrix is singular or non-singular.
Singular matrix: The determinant (ad-bc) is 0.
Non Singular matrix: The determinant (ad-bc) is not 0.
'''

#This is the function to calculate the cofactor of a matrix
def CalculateCofactor(mtrx, a, b):
    return [row[: b] + row[a+1:] for row in (mtrx[: a] + mtrx[a+1:])]

#This is the function to check whether the matrix is singular or non singular
def IsSingular(mtrx):
    n = len(mtrx)
    if (n == 2):
        v = mtrx[0][0]*mtrx[1][1] - mtrx[1][0]*mtrx[0][1] #This is the determinant formula for the matrix
        return v

    #calculating the determinant of matrix using cofactor
    dtm = 0
    for a in range(n):
        s = (-1)**a
        subdtm = IsSingular(CalculateCofactor(mtrx, 0, a))
        dtm += (s*mtrx[0][a]*subdtm)
    return dtm

