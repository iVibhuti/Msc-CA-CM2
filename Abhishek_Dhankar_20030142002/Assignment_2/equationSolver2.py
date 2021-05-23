import numpy as np

def equationSolver2(nonAugmentedMatrix):
  # finding free variable
  # for i in range(0, len(nonAugmentedMatrix)):
  #   if nonAugmentedMatrix[i][i] == 0:
  #     free_variable = i
  #     # print(f"free variable: {free_variable}")
  #     break

  # making changes to the original matrix for the free variable
  # preparing a
  a = nonAugmentedMatrix[:]
  # a[len(nonAugmentedMatrix)-1][free_variable] = 1
  b = []
  # preparing b
  for i in range(0,len(nonAugmentedMatrix)):
    b.append(0)
  b[len(nonAugmentedMatrix)-1] = 1

  a = np.array(a)
  b = np.array(b)
  x = np.linalg.solve(a, b)
  return x