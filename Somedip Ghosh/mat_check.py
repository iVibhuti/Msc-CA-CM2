def cofac(mat, i, j):
    return [row[: j] + row[j+1:] for row in (mat[: i] + mat[i+1:])]

def t_sing(mat):
    l = len(mat)
    if (l == 2):
        val = mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
        return val
    
    determinant = 0
    for i in range(l):
        s = (-1)**i
        sub_determinant = t_sing(cofac(mat, 0, i))
        determinant += (s*mat[0][i]*sub_determinant)
    return determinant

