import math
import numpy as np
from UnitTestCases import OrthoGS
from UnitTestCases import SolveEq
from UnitTestCases import SolveEq2
from UnitTestCases import RowEchelon


#============================= Eigen Values Test Case =============================
def EigenValueCalc(Matrix):
	Values, Vectors = np.linalg.eig(Matrix)
	ListValues = list(Values)
	for v in range(0, len(ListValues)):
	    if ListValues[v]<0:
	        ListValues[v] = 0
	    ListValues[v] = round(ListValues[v])
	ListValues.sort()
	return np.array(ListValues[::-1])


#============================= Eigen Vector Test Case =============================
def EigenVectorCalc(dotProductMatrix, lambda_):
  PreparedMatrix = dotProductMatrix[::]
  for i in range(0,len(dotProductMatrix)):
    PreparedMatrix[i][i] = PreparedMatrix[i][i] - lambda_
  N = len(PreparedMatrix)
  a = np.array(PreparedMatrix)
  b = np.zeros((N,N+1))
  b[:,:-1] = a
  RowReduceEcholenForm = RowEchelon(b)
  # removing augmentation
  n_rows, n_cols = RowReduceEcholenForm.shape
  RowReduceEcholenForm = np.delete(RowReduceEcholenForm, n_cols-1, 1)
  # solving the equation to get the eigen Vector
  Vector = SolveEq(RowReduceEcholenForm.tolist())
  FinalVector = OrthoGS(Vector)
  return FinalVector


#============================= Solve Equation Test Case =============================
def SolveEq(NonAugmentedMatrix):
  for i in range(0, len(NonAugmentedMatrix)):
    if NonAugmentedMatrix[i][i] == 0:
      free_variable = i
      break
  a = NonAugmentedMatrix[:]
  a[len(NonAugmentedMatrix)-1][free_variable] = 1
  b = []
  for i in range(0,len(NonAugmentedMatrix)):
    b.append(0)
  b[len(NonAugmentedMatrix)-1] = 1
  a = np.array(a)
  b = np.array(b)
  x = np.linalg.solve(a, b)
  return(x)

def SolveEq2(NonAugmentedMatrix):
  a = NonAugmentedMatrix[:]
  b = []
  for i in range(0,len(NonAugmentedMatrix)):
    b.append(0)
  b[len(NonAugmentedMatrix)-1] = 1
  a = np.array(a)
  b = np.array(b)
  x = np.linalg.solve(a, b)
  return x


#============================= Orthogonal Matrix Test Case =============================
#================================ G Schmidt Orthogonal =================================
def OrthoGS(Vector):
    dist = 0
    for v in Vector:
        dist = dist+(v**2)
    dist = math.sqrt(dist)
    for i in range(0, len(Vector)):
        Vector[i] = Vector[i]/dist
    return Vector


#============================= Read File Test Case =============================
def ReadFile(FileName):
  with open(FileName, 'r') as Input:
    FileData = Input.read()
    return FileData
def CreateMatrix(FileData):
  FileData = FileData+'\n'
  Matrix = []
  Number = ''
  row = []
  try:
    if int(FileData) or int(FileData) == 0:
      row.append(int(FileData))
      Matrix.append(row)
      return Matrix

  except ValueError:
    for item in FileData:
      try:
        if item != ',' and item != '\n':
          Number = Number + item
        elif item == ',':
          row.append(int(Number))
          Number = ''
        elif item == '\n':
          if row == []:
            continue
          else:
            row.append(int(Number))
            Number = ''
            Matrix.append(row)
            row = []
      except ValueError:
        return "Matrix in 'Input.txt' is not in proper format. Please! check."     
    return(Matrix)



#============================= Row Reduction Test Case =============================
def EigenVectorCalc2(dotProductMatrix, lambda_):
  PreparedMatrix = dotProductMatrix[::]
  for i in range(0,len(dotProductMatrix)):
    PreparedMatrix[i][i] = PreparedMatrix[i][i] - lambda_
  N = len(PreparedMatrix)
  a = np.array(PreparedMatrix)
  b = np.zeros((N,N+1))
  b[:,:-1] = a
  # Reducing the Matrix to row Echelon form
  RowReduceEcholenForm = RowEchelon(b)
  # Removing Augmentation
  n_rows, n_cols = RowReduceEcholenForm.shape
  RowReduceEcholenForm = np.delete(RowReduceEcholenForm, n_cols-1, 1)
  Vector = SolveEq2(RowReduceEcholenForm.tolist())
  FinalVector = OrthoGS(Vector)
  return FinalVector

def RowEchelon(A):
    """ Return Row Echelon Form of Matrix A """
    r, c = A.shape
    if r == 0 or c == 0:
        return A
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        B = RowEchelon(A[:,1:])
        return np.hstack([A[:,:1], B])
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row
    A[0] = A[0] / A[0,0]
    A[1:] -= A[0] * A[1:,0:1]
    B = RowEchelon(A[1:,1:])
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])
    A = np.array([[1,-0.442,0],[0,1,0]], dtype='float')
    return A


#============================= Reduced Row Echelon Form Test Case =============================
def RowEchelon(B, tol=1e-8, debug=False):
  A = B.copy()
  rows, cols = A.shape
  r = 0
  Pivots_pos = []
  RowExchange = np.arange(rows)
  for c in range(cols):
    Pivot = np.argmax (np.abs (A[r:rows,c])) + r
    m = np.abs(A[Pivot, c])
    if m <= tol:
      A[r:rows, c] = np.zeros(rows-r)
    else:
      Pivots_pos.append((r,c))
      if Pivot != r:
        A[[Pivot, r], c:cols] = A[[r, Pivot], c:cols]
        RowExchange[[Pivot,r]] = RowExchange[[r,Pivot]]
      A[r, c:cols] = A[r, c:cols] / A[r, c];
      v = A[r, c:cols]
      if r > 0:
        ridx_above = np.arange(r)
        A[ridx_above, c:cols] = A[ridx_above, c:cols] - np.outer(v, A[ridx_above, c]).T
      if r < rows-1:
        ridx_below = np.arange(r+1,rows)
        A[ridx_below, c:cols] = A[ridx_below, c:cols] - np.outer(v, A[ridx_below, c]).T
      r += 1
    if r == rows:
      break;
  return (A)