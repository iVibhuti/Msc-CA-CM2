from Singular_Matrix_Check import *
import unittest
class Test_Matrix_Singular(unittest.TestCase):
    # Test Case function to check  if the given matrix is singular or not
    def test_singular(self):

        # TEST CASES PASSED(Singular matrix => matrix=0 )
##        self.assertEqual(check_singular(matrix=[[78, 45, 4], [0, 0, 0], [7, 4, -54]]),0) #PASS
##        self.assertEqual(check_singular(matrix=[[1, 4, 1], [1, 6, 1], [1, 7, 1]]),0) #PASS
##        self.assertEqual(check_singular(matrix=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]),0) #PASS
##        self.assertEqual(check_singular(matrix=[[54, 0, 6], [4, 0, 27], [6, 0, 9]]),0)#PASS

        # TEST CASES FAILED(Non-Singular matrix => matrix !=0 )
##        self.assertEqual(check_singular(matrix=[[2, 1, 1], [1, 2, 1], [1, 1, 1]]),0)#FAIL
##        self.assertEqual(check_singular(matrix=[[24, 3, 6], [11, 7, 27], [6, 12, 9]]),0)#FAIL
##        self.assertEqual(check_singular(matrix=[[4, 3, 8], [1, 3, 7], [6, 5, 3]]),0)#FAIL
##        self.assertEqual(check_singular(matrix=[[1, 5, 7], [6, 23, 4], [4, 46, 81]]),0)#FAIL


#To Execute The Test Case

if __name__ == '__main__':
    unittest.main()
