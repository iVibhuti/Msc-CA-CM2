#A matrix is said to be a singular matrix if its determinant is equal to zero.

#Function to get cofactor of matrix[i][j].
def cofactor(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]

#Recursive function to check if matrix is singular or not.
def check_singular(matrix):
    data=len(matrix)
    if (data== 2):
        result = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return result
    
    determinant = 0
    for i in range(data):
        val= (-1)**i
        dt = check_singular(cofactor(matrix, 0, i))
        determinant += (val*matrix[0][i]*dt)
    return determinant

