# a given matrix is a singular matrix or not in Python.
#  A matrix is said to be a singular matrix if its determinant is equal to zero.

#This function for to get cofactor of matrix[i][j].
def cofactor(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]

# This function is to check wheather matrix is singular or not.
def is_singular(matrix):
    n = len(matrix)  # n is the data 
    if (n == 2):
        val = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]   # Applying the Formula of determine in val 
        return val

# Declare a variable det to store the determinant.
   
    det = 0  # det means determinant 
    # Apply the formula and store the result in det. Finally, return the determinant.
    for i in range(n):
        s = (-1)**i
        sub_det = is_singular(cofactor(matrix, 0, i))   
        det += (s*matrix[0][i]*sub_det)
    return det
