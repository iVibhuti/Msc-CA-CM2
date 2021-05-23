import numpy as np
from sympy import *

def row_echelon_form(mat5):
    M = Matrix(mat5.tolist())

    M_rref, abc = M.rref()  
 
    return M_rref