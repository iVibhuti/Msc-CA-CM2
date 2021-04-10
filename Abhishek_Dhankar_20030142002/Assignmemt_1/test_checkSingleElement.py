import unittest
from readFromInput import createMatrix
from checkSingleElement import isSingleElement

class Test_checkSingleElement(unittest.TestCase):
	def testIfsingleElement(self):
		matrix = createMatrix("1")
		result = isSingleElement(matrix)
		self.assertEqual(result, True)

	def testIfNotSingle(self):
		matrix = createMatrix("1,2\n3,4")
		result = isSingleElement(matrix)
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()