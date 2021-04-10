import unittest
from readFromInput import createMatrix

class Test_readFromInput(unittest.TestCase):

	def test_matrixFormat1(self):
		fileString = "a,1\n2,3"
		result = createMatrix(fileString)
		self.assertEqual(result, "Matrix in 'input.txt' is not in proper format. Please! check.")

	def test_matrixFormat2(self):
		fileString = "1,2,\n3,4"
		result = createMatrix(fileString)
		self.assertEqual(result, "Matrix in 'input.txt' is not in proper format. Please! check.")

	def test_matrixFormat3(self):
		fileString = "1,\n,2,3"
		result = createMatrix(fileString)
		self.assertEqual(result, "Matrix in 'input.txt' is not in proper format. Please! check.")

	def test_matrixFormat4(self):
		fileString = "1,2,3\n4,5,6\n7,8,9,"
		result = createMatrix(fileString)
		self.assertEqual(result, "Matrix in 'input.txt' is not in proper format. Please! check.")

if __name__ == '__main__':
    unittest.main()