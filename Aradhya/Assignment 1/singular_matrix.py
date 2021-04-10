# Taking the input matrix from reading the file
def InputMatrix(filename):
    with open (filename, "r") as file:
        data = []
        for row in file:
            data.append([int(x) for x in row.split(",")])

    return data
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
# Main function
if __name__ == '__main__':
    input = InputMatrix("input.txt")
    print("Printing the matrix: ")
    print(input)

    n = 3
    if (check_for_singular(matrix)):
        print("Matrix is non-singular")
    else:
        print("Matrix is singular")