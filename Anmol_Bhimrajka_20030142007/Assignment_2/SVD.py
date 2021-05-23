import numpy as np  
from sympy import *
import math

# Reading the file 
def InputMatrix(filename):
    with open (filename, "r") as file:
        data = []
        for row in file:
            data.append([int(x) for x in row.split(",")])

    return data  

# Function for V
def singularValueDicomposition_v(mat):

    mat1 = np.matrix(mat)
    v_matrix = np.dot(mat1.T, mat1)
    print("printing dot matrix\n", v_matrix)

    eigen_values = eigenvalues(v_matrix)
    print("Printing the eigenvalue for A(t)XA\n", eigen_values, "\n")

    Sigma = np.sqrt(eigen_values)
    print("Printing the Sigma\n", Sigma, "\n")

    eigen_vector = []
    for i in eigen_values:
        eigen_vector.append(eigenvector(np.dot(mat1.T, mat1), i).tolist())
    
    print("Value of V = \n", eigen_vector, "\n")

# Function for U
def singularValueDicomposition_u(mat):

    mat1 = np.matrix(mat)
    v_matrix = np.dot(mat1, mat1.T)
    print("printing dot matrix\n", v_matrix)

    eigen_values = eigenvalues(v_matrix)
    print("Printing the eigenvalue for A(t)XA\n", eigen_values)

    eigen_vector = []
    for i in eigen_values:
        eigen_vector.append(eigenvector(np.dot(mat1, mat1.T), i).tolist())
    
    print("Value of U= \n", eigen_vector, "\n")

# Computing the Eigenvalue
def eigenvalues(mat):
    w, v = np.linalg.eig(mat) 
    #print( "Eigenvalues of the said matrix",w)
    #print( "Eigenvectors of the said matrix",v)
    w = np.sort(w)
    my_list = w.tolist()
    return np.array(my_list[::-1])


def eigenvector(mat3, lam):

    mat4 = mat3.tolist()
    for i in range(0, len(mat3)):
        mat4[i][i] = mat4[i][i] - lam
    


    n = len(mat4)
    x = np.array(mat4)
    y = np.zeros((n, n+1))
    y[:,:-1] = x

    echelon_form_new = row_echelon_form(y)


    n_roww, n_coll = echelon_form_new.shape
    echelon_form_new = np.delete(echelon_form_new, n_coll-1, 1)


    equation = solve_equation(np.array(echelon_form_new))

    equations = equation
    dist = 0 
    for i in equations:
        dist = dist + (i**2)
    dist = math.sqrt(dist)

    for x in range(0, len(equations)):
        equations[x] = equations[x]/dist
    return equations


def row_echelon_form(mat5):
    M = Matrix(mat5.tolist())

    M_rref, abc = M.rref()  
 
    return M_rref


def solve_equation(mat6):
    mat6 =  mat6.tolist()

    for i in range(0, len(mat6)):
        if mat6[i][i] == 0:
            free_v = i
            break

    a = mat6[:]
    a[len(mat6)-1][free_v] = 1
    b = []

    for i in range(0, len(mat6)):
        b.append(0)
    b[len(mat6)-1] = 1
    
    a = np.array(a).astype(float)
    b = np.array(b).astype(float)

    x = np.linalg.solve(a, b)
    
    return(x)


# Main function
if __name__ == '__main__':
    input = InputMatrix("input.txt")
    print("Printing the matrix: ")
    print(input)

   
    singularValueDicomposition_v(input)
    singularValueDicomposition_u(input)
