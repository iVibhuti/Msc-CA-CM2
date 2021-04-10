#Function to get cofactor of particular elment in a matrix
def mat_cofactor(matrix, i, j):
    return [r[: j] + r[j+1:] for r in (matrix[: i] + matrix[i+1:])]

#Function to find determinant of matrix and return the dterminant to calling function
def check_singular(matrix):
    #find the length of a matrix
    size = len(matrix)

    #If it is a 2x2 matrix following code executes and returns the determinant 
    if (size == 2):
        d = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return d
    
    #If it is a 3x3 matrix or greater following code executes and returns the determinant 
    d = 0
    for i in range(size):
        s = (-1)**i
        sub_d = check_singular(mat_cofactor(matrix, 0, i))
        d += (s*matrix[0][i]*sub_d)
    return d

