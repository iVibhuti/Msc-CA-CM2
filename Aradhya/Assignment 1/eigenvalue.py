import numpy as np
import math

#Computing the Eigenvalue

def eigenvalues(mat):
    w, v = np.linalg.eig(mat) 
    #print( "Eigenvalues of the said matrix",w)
    #print( "Eigenvectors of the said matrix",v)
    w = np.sort(w)
    my_list = w.tolist()
    return np.array(my_list[::-1])