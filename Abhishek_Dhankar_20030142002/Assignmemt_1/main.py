from readFromInput import readFile, createMatrix
from calculateDeterminant import determinantOfMatrix
from checkSquareMatrix import isSquare
from checkIdentityMatrix import isIdentityMatrix
from checkZeroMatrix import isZeroMatrix
from checkSingleElement import isSingleElement

matrix = createMatrix(readFile("inputFile.txt"))

if not isinstance(matrix, list):
	outputString = matrix
	outputStringLength = len(outputString)
	print("\n", "-"*outputStringLength)
	print(f"{matrix}")
	print("-"*outputStringLength,"\n")

elif isSingleElement(matrix):
	outputString = f"{matrix} is a single element Matrix"
	outputStringLength = len(outputString)
	print("\n","-"*outputStringLength)
	print(outputString)
	print("-"*outputStringLength,"\n")

else:
	if not isSquare(matrix):
		outputString = f"{matrix} is not a square matrix And its determinant cannot be calculated."
		outputStringLength = len(outputString)
		print("\n","-"*outputStringLength)
		print(outputString)
		print("-"*outputStringLength,"\n")

	else:
		if isIdentityMatrix(matrix):
			outputString = f"{matrix} is an Identity matrix."
			outputStringLength = len(outputString)
			print("\n","-"*outputStringLength)
			print(outputString)
			print("-"*outputStringLength,"\n")
		elif isZeroMatrix(matrix):
			outputString = f"{matrix} is a Zero matrix."
			outputStringLength = len(outputString)
			print("\n","-"*outputStringLength)
			print(outputString)
			print("-"*outputStringLength,"\n")
		else:
			determinant = determinantOfMatrix(matrix)
			print("\n---------------------------------------------------------------------")

			print(f"  The matrix {matrix} is ",end=" ")

			if determinant != 0:
			  print("\"non-Singular\"")
			else:
			  print("\"Singular\"")

			print("---------------------------------------------------------------------\n")