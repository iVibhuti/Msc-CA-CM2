import numpy as np  
from sympy import *
import math
from eigenvalue import eigenvalues
from eigenvector import eigenvector

# Reading the file 
def InputMatrix(filename):
    with open (filename, "r") as file:
        data = []
        for row in file:
            data.append([int(x) for x in row.split(",")])

    return data  

# Function for V
def singularValueDecomposition_v(mat):

    mat1 = np.matrix(mat)
    v_matrix = np.dot(mat1.T, mat1)
    print("Dot matrix is :\n", v_matrix)

    eigen_values = eigenvalues(v_matrix)
    print("Eigenvalue for A(t)XA\n", eigen_values)

    eigen_vector = []
    for i in eigen_values:
        eigen_vector.append(eigenvector(np.dot(mat1.T, mat1), i).tolist())
    
    print("Value of V = \n", eigen_vector, "\n")

# Function for U
def singularValueDecomposition_u(mat):

    mat1 = np.matrix(mat)
    v_matrix = np.dot(mat1, mat1.T)
    print("Dot matrix is :\n", v_matrix)
    
    eigen_values = eigenvalues(v_matrix)
    print("Eigenvalue for A(t)XA\n", eigen_values)
   
    eigen_vector = []
    for i in eigen_values:
        eigen_vector.append(eigenvector(np.dot(mat1, mat1.T), i).tolist())
    
    print("Value of U= \n", eigen_vector, "\n")




# Main function
if __name__ == '__main__':
    input = InputMatrix("input.txt")
    print("Input matrix is : ")
    print(input)

   
    singularValueDecomposition_v(input)
    singularValueDecomposition_u(input)
