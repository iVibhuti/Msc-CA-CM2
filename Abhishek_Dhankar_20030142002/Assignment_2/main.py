from readFromInput import readFile, createMatrix
from eigenValues import calculateEigenValues
from eigenVector import calEigenVector
import numpy as np
from rowReduce2 import calEigenVector2

matrix = createMatrix(readFile("inputFile.txt"))

if not isinstance(matrix, list):
	outputString = matrix
	outputStringLength = len(outputString)
	print("\n", "-"*outputStringLength)
	print(f"{matrix}")
	print("-"*outputStringLength,"\n")

else:
	print(f"\nFactors are represented as: A = U.Sigma.V(transpose)\n")
	# A matrix can be represented into factors as 
	# U.sigma.V(transpose)
	matrix = np.array(matrix)
	print(f"Our Matrix:\n{matrix}\n")

	# calculating V
	# calculate A(transpose).A
	# print(f"matrix.T\n{matrix.T}")
	# print(f"matrix\n{matrix}")
	v_dot_matrix = np.dot(matrix.T, matrix)
	# print(f"A(transpose).A:\n{v_dot_matrix}")
	v_eigenValues = calculateEigenValues(v_dot_matrix)
	# print(f"eigen values for A(transpose).A:\n{v_eigenValues}")
	#now calculate the eigen vectors
	v_eigen_vectors = []
	try:
		for ll in v_eigenValues:
			v_eigen_vectors.append(calEigenVector(np.dot(matrix.T, matrix),ll).tolist())
		# print(f"V matrix:\n{np.array(v_eigen_vectors).T}")
	except:
		for l in v_eigenValues:
			v_eigen_vectors.append(calEigenVector2(np.dot(matrix.T, matrix),l).tolist())

	# calculating U
	# calculate A.A(transpose)
	u_dot_matrix = np.dot(matrix,matrix.T)
	# print(f"A.A(transpose):\n{u_dot_matrix}")
	u_eigenValues = calculateEigenValues(u_dot_matrix)
	# print(f"eigen values for A.A(transpose):\n{u_eigenValues}")
	# now calculate the eigen vectors
	u_eigen_vectors = []
	try:
		for ll in u_eigenValues:
			u_eigen_vectors.append(calEigenVector(np.dot(matrix, matrix.T),ll).tolist())
		# print(f"U matrix:\n{np.array(u_eigen_vectors).T}")
	except:
		for l in u_eigenValues:
			u_eigen_vectors.append(calEigenVector2(np.dot(matrix, matrix.T),l).tolist())


	# calculating sigma matrix
	sigma = np.diag(np.array(v_eigenValues),k=0)
	sigma = np.sqrt(sigma)
	# print(f"Sigma matrix:\n{sigma}")

	print(f"U matrix:\n{np.array(u_eigen_vectors).T}\n")
	print(f"Sigma matrix:\n{sigma}\n")
	print(f"V matrix:\n{np.array(v_eigen_vectors).T}\n")
