# Taking the input matrix from reading the file
def inputMatrix(filename):
    with open (filename, "r") as file:
        matrix = []
        for row in file:
            matrix.append([int(x) for x in row.split(",")])

    return matrix


#Function to get cofactor of matrix[i][j].
def getcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
 
#Recursive function to check if matrix is singular or not.

def determinantOfMatrix(mat):
 
    if(len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
 
    # initialize Sum to zero
    Sum = 0
 
    for current_column in range(len(mat)):
 
        sign = (-1) ** (current_column)
 
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
 
        Sum += (sign * mat[0][current_column] * sub_det)
 
    # returning the final Sum
    return Sum


# Taking the input matrix from reading the file
matrix = inputMatrix("input.txt")
determinant = determinantOfMatrix(matrix)

if(determinant != 0):
    print("Matrix is non-Singular.")
else:
    print("Matrix is Singular.")
