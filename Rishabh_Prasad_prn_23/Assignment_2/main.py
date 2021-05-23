import numpy as np
from numpy import array
from numpy import diag
from numpy import dot
from numpy import zeros
from numpy import linalg as LA
from scipy import linalg
import math


def cal_SVD(trans_matrix):
    
    #matrix * matrix^T
    print("\n======================================")
    print("Calculation for A * A^T")
    print("======================================\n\n")
    ori_matrix = trans_matrix

    #finding transpose of the original matrix
    result = [[trans_matrix[j][i] for j in range(len(trans_matrix))] for i in range(len(trans_matrix[0]))]

    #product of original matrix and transpose matrix
    m_product = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*result)] for X_row in ori_matrix]
    
    #finding eigen values and eigen vectors
    a1, b1=np.linalg.eig(m_product)

    #finding summation
    v1 = math.sqrt(a1[0])
    v2 = math.sqrt(a1[1])
    s = array([[v2,0],[0,v1]])

    #printing the values for A . A^T
    print("Eigen values of the matrix = ",a1,"\n")
    print("The Summation = \n",s,"\n") 
    print("Eigen vectors of the matrix (U) = \n",b1,"\n")
    print("======================================")
   


    #matrix^T * matrix
    print("Calculation for A^T * A")
    print("======================================\n")

    #product of transpose matrix and original matrix
    m_product = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*ori_matrix)] for X_row in result]
   
    #finding eigen values and eigen vectors
    a2, b2=np.linalg.eig(m_product)
    
    #calculating summation
    v3 = math.sqrt(a2[0])
    v4 = math.sqrt(a2[1])
    s2 = array([[v3,0],[0,v4]])

    #printing the values for A^T . A
    print("Eigen values of the matrix = ",a2,"\n")
    print("The Summation = \n",s2,"\n")
    print("Eigen vectors of the matrix (V) = \n",b2,"\n")

    print("====================================================")
    print("THE FINAL OUTPUT:")
    print("====================================================\n")
    print(" U = \n",b1,"\n\n","Summation = \n",s2,"\n\n","V = \n",b2)
    print("\n\n====================================================")



   # Main function
if __name__ == '__main__':
    ori_matrix = np.array([[4,0],[3,-5]])
    print("\n\n======================================")
    print("\n The original matrix A = ",ori_matrix,"\n")
    print("======================================")
    
    cal_SVD(ori_matrix)
    

 

    


