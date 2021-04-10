import unittest
from readFromInput import createMatrix
from checkIdentityMatrix import isIdentityMatrix

class Test_checkIdentityMatrix(unittest.TestCase):

	def test_ifIdentityMatrix1(self):
		matrix = createMatrix("1,0\n0,1")
		result = isIdentityMatrix(matrix)
		self.assertEqual(result, True)

	def test_ifIdentityMatrix2(self):
		matrix = createMatrix("1,0,0\n0,1,0\n0,0,1")
		result = isIdentityMatrix(matrix)
		self.assertEqual(result, True)

	def test_ifNotIdentityMatrix1(self):
		matrix = createMatrix("1,2\n3,4")
		result = isIdentityMatrix(matrix)
		self.assertEqual(result, False)

	def test_ifNotIdentityMatrix2(self):
		matrix = createMatrix("1,2,4\n3,4,6")
		result = isIdentityMatrix(matrix)
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()