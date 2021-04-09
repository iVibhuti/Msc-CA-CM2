def getCofactor(M, temp, p, q, n):
    i = 0
    j = 0
  
    for row in range(n): 
          
        for col in range(n):
              
           
            if (row != p and col != q) :
                  
                temp[i][j] = M[row][col]
                j += 1
  
               
                if (j == n - 1):
                    j = 0
                    i += 1
  

def determinantMatrix(mat, n):
    D = 0 
    if (n == 1):
        return mat[0][0]
          
   
    temp = [[0 for x in range(N)] 
               for y in range(N)] 
  
    sign = 1 
  
    for f in range(n):
          
        getCofactor(mat, temp, 0, f, n)
        D += (sign * mat[0][f] *
              determinantMatrix(temp, n - 1))
  
        
        sign = -sign
    return D
  
def isInvertible(M, n):
    if (determinantMatrix(M, N) != 0):
        return True
    else:
        return False
      
M = []
with open('D:\\Msc CA Section\\Sem 2\\Computational Methods\\Inverse Matrix\\input.txt', 'r') as f:
    M = [[int(num) for num in line.split(',')] for line in f]

print("Original Matrix\n",M)

N = 3
if (isInvertible(M, N)):
    print("Singular Matrix")
else:
    print("Non Singular Matrix")
  
