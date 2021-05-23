import numpy as np
import math
from row_echelon_form import row_echelon_form
from solveequation import solve_equation


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