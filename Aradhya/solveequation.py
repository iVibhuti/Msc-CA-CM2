import numpy as np
import math

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
