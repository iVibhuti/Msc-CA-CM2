def get_cofactor(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]

def is_singular(matrix):
    n = len(matrix)
    if (n == 2):
        val = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return val
    
    det = 0
    for i in range(n):
        s = (-1)**i
        sub_det = is_singular(get_cofactor(matrix, 0, i))
        det += (s*matrix[0][i]*sub_det)
    return det

