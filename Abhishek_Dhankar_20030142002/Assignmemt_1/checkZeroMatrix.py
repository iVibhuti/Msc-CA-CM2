def isZeroMatrix(matrix):
	#calculate number of rows
	rows = len(matrix)

	#calculate number of columns
	cols = len(matrix[0])

	for i in range(0, rows):
		for j in range(0, cols):
			if matrix[i][j] != 0:
				return False
	return True