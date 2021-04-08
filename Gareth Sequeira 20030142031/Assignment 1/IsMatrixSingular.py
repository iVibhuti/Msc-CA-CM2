InputFile = []
with open('G:\\Gareth\\SICSR\\Sem2\\CM\\Assignment 1\\Input.txt', 'r') as f:
    InputFile = [[int(num) for num in line.split(',')] for line in f]

def Cofactor(Matrix, i, j):
    return [row[: j] + row[j+1:] 
    for row in (Matrix[: i] + Matrix[i+1:])]

def NonSingular(Matrix):
    n = len(Matrix)
    if (n == 2):
        Value = Matrix[0][0]*Matrix[1][1] - Matrix[1][0]*Matrix[0][1]
        return Value
    
    Determinant = 0
    for i in range(n):
        S = (-1)**i
        SDeterminant = NonSingular(Cofactor(Matrix, 0, i))
        Determinant += (S*Matrix[0][i]*SDeterminant)
    return Determinant


Matrix = InputFile
n = len(Matrix)
print("\nOriginal Matrix is: ")
for i in range(n):
    for j in range(n):
        print(Matrix[i][j], end=' ')
    print()
if(NonSingular(Matrix)):
    print("\nThe Above Matrix is Non-Singular.")
else:
    print("\nThe Above Matrix is Singular\n")