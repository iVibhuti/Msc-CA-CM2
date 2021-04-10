from Singular_matrix import check_singular
import unittest

class Test_singular(unittest.TestCase):

    def test_singular(self):
        matrix1=[[4,10,1],[0,0,0],[1,4,-3]]
        matrix2=[[78,45,4],[0,0,0],[7,4,-54]]
        # Test case passes for both the matrix as their determinant is 0
        self.assertEqual(check_singular(matrix1,3), 0) 
        self.assertEqual(check_singular(matrix2,3), 0)
        # # when we change value to 4 test case will fail 
        # # as 0 = 4 FAILS
        # self.assertEqual(check_singular(matrix1,3), 4) 
        # self.assertEqual(check_singular(matrix2,3), 4)



    def test_non_singular(self):

        # Matrix given are non _ singular
        # when we run test case it check determinant is not equal 0
        # condition become true
        matrix3=[[5,9,6],[3,7,8],[21,55,6]]
        matrix4=[[0,2,-1],[3,-2,1],[3,2,1]] 

        # when we give singular matrix
        # it failed the test as 0 != 0  FAILS
        #matrix4=[[78,45,4],[0,0,0],[7,4,-54]]

        # Test case pases for both the matrix as their determinant is 0
        self.assertNotEqual(check_singular(matrix3,3), 0, "not singular")
        self.assertNotEqual(check_singular(matrix4,3), 0, "not singular")

if __name__ == '__main__':
    unittest.main()