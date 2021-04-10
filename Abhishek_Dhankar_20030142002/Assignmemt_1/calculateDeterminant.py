
# defining a function to get the minor matrix by ignoring ith row and jth column.
def findcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(matrix):
 
    # if the matrix is of dimension 2X2. Return determinant starght away.
    if(len(matrix) == 2):
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value
 
    # initialize Sum to zero
    Sum = 0
 
    # loop to traverse each column
    # of matrix a.
    for column in range(len(matrix)):
 
        # calculating the sign
        sign = (-1) ** (column)
 
        # need to use recursion
        sub_det = determinantOfMatrix(findcofactor(matrix, 0, column))
 
        # adding the calculated determinant
        Sum += (sign * matrix[0][column] * sub_det)
 
    return Sum