import numpy as np
from rowReduceEcholenForm import row_echelon
from equationSolver2 import equationSolver2
from ortho import gs


def calEigenVector2(dotProductMatrix, lambda_):
  # print(f"dotProductMatrix: {dotProductMatrix}")
  # prepare the matrix
  prepared_matrix = dotProductMatrix[::]
  for i in range(0,len(dotProductMatrix)):
    prepared_matrix[i][i] = prepared_matrix[i][i] - lambda_
  # print(f"prepared_matrix: \n{prepared_matrix}")
  # print(f"lambda_:\n{lambda_}")
  
  # print(f"Prepared Matrix: {prepared_matrix}")
  # making the prepared matrix augmented
  N = len(prepared_matrix)
  a = np.array(prepared_matrix)
  b = np.zeros((N,N+1))
  b[:,:-1] = a
  # print(f"b:\n{b}")
  # reducing the matrix into row echelon form
  row_reduce_echolen_form = row_echelon(b)
  # print(f"rref:\n{row_reduce_echolen_form}")

  # removing augmentation
  n_rows, n_cols = row_reduce_echolen_form.shape
  row_reduce_echolen_form = np.delete(row_reduce_echolen_form, n_cols-1, 1)
  # print(f"removing augmentation:\n{row_reduce_echolen_form}")
  # solving the equation to get the eigen vector
  # remove fractional (0.5455) to 0
  # print(f"solving equation for:\n{row_reduce_echolen_form}")
  vector = equationSolver2(row_reduce_echolen_form.tolist())
  # print(f"vector after solving equatin:\n{vector}")
  final_vector = gs(vector)
  
  return final_vector

def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

    A = np.array([[1,-0.442,0],[0,1,0]], dtype='float')

    return A