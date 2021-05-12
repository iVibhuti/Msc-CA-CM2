def mat(arr, i, j):
    return [row[: j] + row[j+1:] for row in (arr[: i] + arr[i+1:])]

# Recursive function to check if matrix is singular or not.


def check_singular(arr):
    data = len(arr)
    if (data == 2):
        res = arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1]
        return res

    determinant = 0
    for i in range(data):
        val = (-1)**i
        dt = check_singular(mat(arr, 0, i))
        determinant += (val*arr[0][i]*dt)
    return determinant
