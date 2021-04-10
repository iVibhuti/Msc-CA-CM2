def isSquare(matrix):
	rows = len(matrix)

	for i in range(0, rows):
		column = len(matrix[i])
		if rows != column:
			return False
	return True