from invertible import *
#To test invertible.py with different inputs
import unittest
class invertibleUnittest(unittest.TestCase):
    def testCallFunctions(self):
        #non zero determinant
        #FAILS
        with self.subTest():
            self.assertEqual(callFunctions([[5,-1,2], [1,3,0], [-7,1,5]]), 0)
        with self.subTest():
            self.assertEqual(callFunctions([[1,1,-1], [1,2,3], [-3,4,-5]]), 0)
        with self.subTest():
            self.assertEqual(callFunctions([[6,-1,5], [1,-1,4], [1,-1,7]]), 0)

        # zero value determinant
        #PASSES
        with self.subTest():
            self.assertEqual(callFunctions([[1,2,3], [4,5,6], [7,8,9]]), 0)
        with self.subTest():
            self.assertEqual(callFunctions([[3,2,3], [2,2,3], [3,2,3]]), 0)
        with self.subTest():
            self.assertEqual(callFunctions([[2,7,65], [3,8,75], [5,9,86]]), 0)

        # Unit level testing of 2 functions
        #both pass
        with self.subTest():
            self.assertEqual(getMatrixOfMinor([[1,1,1], [0,2,5], [2,5,-1]]), [[[2.0, 5.0], [5.0, -1.0]], [[0.0, 5.0], [2.0, -1.0]], [[0.0, 2.0], [2.0, 5.0]]])
        with self.subTest():
            self.assertEqual(calculateDeterminant([[1,1,1], [0,2,5], [2,5,-1]], [[[2.0, 5.0], [5.0, -1.0]], [[0.0, 5.0], [2.0, -1.0]], [[0.0, 2.0], [2.0, 5.0]]]), -21.0)
if __name__ == '__main__':
    unittest.main()
