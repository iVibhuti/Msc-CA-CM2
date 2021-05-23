from inverse import *
import unittest
class test_prog(unittest.TestCase):
    # Test Case function to check  if the given matrix is singular or not
    def test(self):
        
# TEST CASES PASSED(Singular matrix => matrix=0 )
        #self.assertTrue(isInvertible(M=[[2, -3, 4], [2, -3, 4], [0, -1, 1]]),True)
#        self.assertTrue(isInvertible(M=[[3, 8, 1], [-4, 1, 1], [-4, 1, 1]]),True)

# TEST CASES FAILED(Non-Singular matrix)
#        self.assertTrue(isInvertible(M=[[1, 3, 8], [3, 3, 7], [8, 5, 1]]),True)
#        self.assertTrue(isInvertible(M=[[51, 4, 1], [67, 3, 4], [5, 6, 1]]),True)

if __name__ == '__main__':
    unittest.main()