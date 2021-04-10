def cofac(mat, x, y):
    return [row[: y] + row[y+1:] for row in (mat[: x] + mat[x+1:])]

def singular_check(mat):
    l = len(mat)
    if (l == 2):
        val = mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
        return val
    
    determine = 0
    for i in range(l):
        s = (-1)**i
        sub_d = singular_check(cofac(mat, 0, i))
        determine += (s*mat[0][i]*sub_d)
    return determine
