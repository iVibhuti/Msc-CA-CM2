from Singualrity_main import *
import unittest


class Test_Matrix_Singular(unittest.TestCase):
    # Test Case function to check  if the given matrix is singular or not
    def test_singular(self):

        # TEST CASES PASSED(Singular matrix => matrix=0 )
        # self.assertEqual(check_singular(matrix=[[78, 45, 4], [0, 0, 0], [7, 4, -54]]),0) #PASS
        # self.assertEqual(check_singular(matrix=[[1, 4, 1], [1, 6, 1], [1, 7, 1]]),0) #PASS
        # self.assertEqual(check_singular(matrix=[[2, 1, -3], [1, 1, 1], [0, -2, 23]]),0) #PASS

        # TEST CASES FAILED(Non-Singular matrix => matrix !=0 )
        # self.assertEqual(check_singular(matrix=[[2, 1, 9], [4, 2, 0], [0, 6, 9]]),0)#FAIL
        # self.assertEqual(check_singular(matrix=[[26, 3, 2], [25, 7, 14], [0, 9, 9]]),0)#FAIL

        # To Execute The Test Case
        if __name__ == '__main__':
            unittest.main()
