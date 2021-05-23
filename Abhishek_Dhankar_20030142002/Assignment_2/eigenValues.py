import numpy as np

def calculateEigenValues(matrix):

	values, vectors = np.linalg.eig(matrix)
	# print(f"values: {values}")
	list_values = list(values)
	for v in range(0, len(list_values)):
	    if list_values[v]<0:
	        list_values[v] = 0
	    list_values[v] = round(list_values[v])
	list_values.sort()
	# print(f"list_values:{list_values}")
	return np.array(list_values[::-1])