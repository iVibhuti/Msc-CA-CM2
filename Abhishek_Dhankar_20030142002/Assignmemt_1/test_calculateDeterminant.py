import unittest
from readFromInput import createMatrix
from calculateDeterminant import determinantOfMatrix

class Test_calculateDeterminant(unittest.TestCase):

	def test_determinant1(self):
		matrix = createMatrix("1,3,2\n-3,-1,-3\n2,3,1")
		result = determinantOfMatrix(matrix)
		self.assertEqual(result, -15)

	def test_determinant2(self):
		matrix = createMatrix("1,2\n3,4")
		result = determinantOfMatrix(matrix)
		self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()