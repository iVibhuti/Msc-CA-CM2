#A matrix is said to be a singular matrix if its determinant is equal to zero.

#Function to get cofactor of matrix[i][j].
def cofactor(matrix, x, y):
    return [row[: y] + row[y+1:] for row in (matrix[: x] + matrix[x+1:])]

#Recursive function to check if matrix is singular or not.
def check_for_singular(matrix):
    n=len(matrix)
    if (n== 2):
        result = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return result

    determinant = 0
    for i in range(data):
        val= (-1)**i
        dt = check_for_singular(cofactor(matrix, 0, i))
        determinant += (val*matrix[0][i]*dt)
    return determinant
