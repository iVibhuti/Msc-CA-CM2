from rowReduceEcholenForm import row_echelon
from equationSolver import equationSolver
from ortho import gs
import numpy as np

def calEigenVector(dotProductMatrix, lambda_):
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
  vector = equationSolver(row_reduce_echolen_form.tolist())
  # print(f"vector after solving equatin:\n{vector}")
  final_vector = gs(vector)
  
  return final_vector