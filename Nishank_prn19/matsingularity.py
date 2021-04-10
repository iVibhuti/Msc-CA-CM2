#func to matrix is singular or non singular
def Sing(mtrx):
    n = len(mtrx)
    if (n == 2):
        v = mtrx[0][0]*mtrx[1][1] - mtrx[1][0]*mtrx[0][1] #determinant
        return v

#calculating the det of matrix using cofactor
    dt = 0
    for a in range(n):
        s = (-1)**a
        sbdt = Sing(Cofactor(mtrx, 0, a))
        dtm += (s*mtrx[0][a]*sbdt)
    return dt

#func to calculate the cofactor of a matrix
def Cofactor(mtrx, a, b):
    return [row[: b] + row[a+1:] for row in (mtrx[: a] + mtrx[a+1:])]