#Creating a function that checks if the matrix 
# has only one element
def isSingleElement(matrix):
	if len(matrix) == 1:
		if(len(matrix[0]) == 1):
			return True
	return False