import numpy as np
from numpy import array
from numpy import diag
from numpy import dot
from numpy import zeros
from numpy import linalg as LA
from scipy import linalg
import math

def getmatrix(fname):
    with open (fname, mode="r") as file:
        value = []
        for row in file:
            value.append([int(x) for x in row.split(",")])
    
    return value

def SVD(Transpose_Matrix):
    
    
    print("===========================================================================")
    print("Calculation for A * A^T")
    print("===========================================================================\n")
    Original_Matrix = Transpose_Matrix
    
    #To Find Transpose of Matrix A:
    cal_trans = [[Transpose_Matrix [j][i] for j in range(len(Transpose_Matrix))] for i in range(len(Transpose_Matrix[0]))]
    
    #To Calculate A*A^T:
    Matrix_Product = [[sum(a*b for a,b in zip(row,col)) for col in zip(*cal_trans)] for row in Original_Matrix]
    
    #To Find Eigenvalues and Eigenvector From A*A^T:
    e, u=np.linalg.eig(Matrix_Product)                  # 'e' is eigenvalues and 'u' is eigenvector for matrix U 
    
    print("Eigen values of a matrix A*A^T =  ",e,"\n")
    
    # To Find Summation: 
    sigma1 = math.sqrt(e[0])                            # calculating squareroot of lamda1                    
    sigma2 = math.sqrt(e[1])                            # calculating squareroot of lamda2
    s = array([[sigma1,0],[0,sigma2]])                  # Putting those values in array
    
    #Print Summation and Matrix of U:
    print("The Summation is = \n",s,"\n")            
    print("From A*A^T Eigen vectors of the matrix for (U) = \n",u,"\n")
    
    
    print("===========================================================================")
    print("Calculation for A^T * A")
    print("===========================================================================\n")

    #To Calculate A^T*A:
    Matrix_Product = [[sum(a*b for a,b in zip(row,col)) for col in zip(*Original_Matrix)] for row in cal_trans]
    
    #To Find Eigenvalues and Eigenvector From A^T*A:
    eig, v=np.linalg.eig(Matrix_Product)                # 'eig' is eigenvalues and 'v' is eigenvector for matrix V
    print("Eigen values of a matrix A^T*A = ",eig,"\n") # Here the output of eigenvalue is in ascending order and in summation matrix it is  
                                                        # always put values in desending order daigonaly for that i have interchange the variable in array function.
                                                        
    #To Find Summation:
    sig1 = math.sqrt(eig[0])                            # calculating squareroot of lamda1       
    sig2 = math.sqrt(eig[1])                            # calculating squareroot of lamda2
    s2 = array([[sig2,0],[0,sig1]])                     # Putinng those values in array (note: the eigen values of both A*A^T and A^T*A are always same )
    V = array([v[1],v[0]])                              
    #Print Summation and Matrix of V:
    print("The Summation is \n",s2,"\n")
    print("From A^T*A Eigen vectors of the matrix for (V) = \n",V,"\n")

    
    print("===========================================================================")
    print("FINAL OUTPUT of SVD :  \n")
    print("===========================================================================")
    print("U = \n",u)                                   # Printing U matrix
    print("\n")
    print("Summation = \n",s)                           # Printing Summation matrix
    print("\n")
    print("V= \n", V)                                   # Printing V matrix
    



   # Main function
if __name__ == '__main__':
    Original_Matrix = getmatrix("mat_input.txt")      # This getmatrix assign to Import the directory file and download the input.txt file from repository  
                                                                                 # and put in same directory where the code is and just copy that address and paste it here.
                                                                                 # Note that input.txt and main.py should be in same directory. 
    print("The original matrix is =  ",Original_Matrix,"\n")
    SVD(Original_Matrix)