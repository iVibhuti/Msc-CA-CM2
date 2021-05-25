import numpy as np
from numpy import array
from numpy import diag
from numpy import dot
from numpy import zeros
from numpy import linalg as LA
from scipy import linalg
import math


def svd(mat):
    
    #matrix * matrix^T
    #finding transpose of the original matrix
    result = mat.T

    #product of original matrix and transpose matrix
    prod = np.dot(mat,result)
    
    #finding eigen values and eigen vectors
    x1, y1=np.linalg.eig(prod)

    #Calculating summation
    a1 = math.sqrt(x1[0])
    a2 = math.sqrt(x1[1])
    sigma1 = array([[a2,0],[0,a1]])

    #printing the values for A . A^T
    print("\n\n Eigen values of the matrix = ",x1,"\n")
    print("\n\n The Sigma = \n",sigma1,"\n") 
    print("\n \n Eigen vectors of the matrix (U) = \n",y1,"\n")
   


    #matrix^T * matrix
    print("Calculation for A^T * A")

    #product of transpose matrix and original matrix
    m_product = np.dot(result,mat)
   
    #finding eigen values and eigen vectors
    x2, y2=np.linalg.eig(m_product)
    
    #calculating summation
    a3 = math.sqrt(x2[0])
    a4 = math.sqrt(x2[1])
    sigma2 = array([[a3,0],[0,a4]])

    #printing the values for A^T . A
    print("Eigen values of the matrix = ",x2,"\n")
    print("The Sigma = \n",sigma2,"\n")
    print("Eigen vectors of the matrix (V) = \n",y2,"\n")

   #FINAL OUTPUT
	
    print("\n\n\n FINAL OUTPUT \n\n\nU = \n",y1,"\n\n","Sigma = \n",sigma2,"\n\n","V = \n",y2)



   # Main function
if __name__ == '__main__':
    original = np.array([[4,0],[3,-5]])
    print("\n The original matrix A = ",original,"\n")
    print("======================================")
    
    svd(original)
    
