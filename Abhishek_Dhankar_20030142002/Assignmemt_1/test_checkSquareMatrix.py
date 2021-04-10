from readFromInput import createMatrix
from checkSquareMatrix import isSquare
import unittest

class Test_checkSquareMatrix(unittest.TestCase):
	def test_ifMatrixIsSquare1(self):
		matrix = createMatrix('1,2\n3,4')
		result = isSquare(matrix)
		self.assertEqual(result, True)

	def test_ifMatrixIsSquare2(self):
		matrix = createMatrix("1,2,3\n4,5,6\n7,8,9")
		result = isSquare(matrix)
		self.assertEqual(result, True)

	def test_ifMatrixIsNotSquare1(self):
		matrix = createMatrix("1,2")
		result = isSquare(matrix)
		self.assertEqual(result, False)

	def test_ifMatrixIsNotSquare2(self):
		matrix = createMatrix("1,2,3\n4,5,6")
		result = isSquare(matrix)
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()