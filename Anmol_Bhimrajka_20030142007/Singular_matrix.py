# Taking the input matrix from reading the file
def InputMatrix(filename):
    with open (filename, "r") as file:
        data = []
        for row in file:
            data.append([int(x) for x in row.split(",")])

    return data  

# Function to get cofactor of matrix[x][y]
def getCofactor(mat,mat2,x,y, n):
    i = 0
    j = 0
      
    # Looping for each element of the matrix
    for row in range(n):
        for col in range(n):
              
            # storing the value in mat2 matrix
            if (row != x and col != y):
                mat2[i][j] = mat[row][col]
                j += 1

                if (j == n - 1):
                    j = 0
                    i += 1
                
def check_singular(mat, n):
    determinant = 0
    # check if dimension of matrix is 2X2
    if(n == 1):
        return mat[0][0]

    mat2 = [[0 for i in range(n + 1)] for i in range(n + 1)]


    # loop to traverse each column of matrix.
    for f in range(n):
        sign = (-1) ** (f)
        getCofactor(mat, mat2, 0, f, n)
        # adding the calculated determinant
        determinant += sign * mat[0][f] * check_singular(mat2, n-1)


    return determinant


# Main function
if __name__ == '__main__':
    input = InputMatrix("input.txt")
    print("Printing the matrix: ")
    print(input)

    n = 3
    if (check_singular(input, n)):
        print("Matrix is non-singular")
    else:
        print("Matrix is singular")
