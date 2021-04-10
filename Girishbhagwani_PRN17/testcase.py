from singular import *
import unittest
class Test_Matrix(unittest.TestCase):
    def test_singular(self):
        # FAILED TEST CASES:
##        self.assertEqual(check_singular(matrix=[[4, 3, 7], [9, 56, 22], [8, 76, 7]]),0)
##        self.assertEqual(check_singular(matrix=[[4, 6, 7], [5, 8, 9], [8, 7, 7]]),0)
##        self.assertEqual(check_singular(matrix=[[44, 66, 7], [78, 8, 80], [87, 76, 72]]),0)

        # PASSED TEST CASES:
##        self.assertEqual(check_singular(matrix=[[0, 66, 75], [0, 65,88], [0, 44, 49]]),0)
##        self.assertEqual(check_singular(matrix=[[2, 4, 6], [2, 0, 2], [6, 8, 14]]),0)
##        self.assertEqual(check_singular(matrix=[[4, 66, 7], [0, 0, 0], [87, 76, 72]]),0)

#Test case execution
if __name__ == '__main__':
    unittest.main()