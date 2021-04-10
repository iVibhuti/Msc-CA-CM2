import unittest
from readFromInput import createMatrix
from checkZeroMatrix import isZeroMatrix

class Test_checkZeroMatrix(unittest.TestCase):

	def test_ifZeroMatrix1(self):
		matrix = createMatrix("0,0\n0,0")
		result = isZeroMatrix(matrix)
		self.assertEqual(result, True)

	def test_ifZeroMatrix2(self):
		matrix = createMatrix("0,0,0\n0,0,0\n0,0,0")
		result = isZeroMatrix(matrix)
		self.assertEqual(result, True)

	def test_ifNotZeroMatrix1(self):
		matrix = createMatrix("0,0\n0,1")
		result = isZeroMatrix(matrix)
		self.assertEqual(result, False)

	def test_ifNotZeroMatrix2(self):
		matrix = createMatrix("0,0,0\n0,1,0\n0,0,0")
		result = isZeroMatrix(matrix)
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()