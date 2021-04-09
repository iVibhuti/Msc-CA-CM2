def cofac(matrix, i, j):
    res=[row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]
    return res
def is_singular(matrix):
    n = len(matrix)
    if (n == 2):
        val = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return val
    
    determinant = 0
    for i in range(n):
        m = (-1)**i
        sdt = is_singular(cofac(matrix, 0, i))
        determinant += (m*matrix[0][i]*sdt)
    return determinant


