def Calculate(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]
def check_singular(matrix):
    n = len(matrix)
    if (n == 2):
        val = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return val
    
    det = 0
    for i in range(n):
        s = (-1)**i
        sub_det = check_singular(Calculate(matrix, 0, i))
        det += (s*matrix[0][i]*sub_det)
    return det
matrix = [[78, 45, 4], [0, 0, 0], [7, 4, -54]]
n = len(matrix)
print("The given matrix")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
if(check_singular(matrix)):
    print("The given matrix is non-Singular")
else:
    print("The given matrix is singular")
