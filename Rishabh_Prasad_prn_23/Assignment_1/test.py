from main_program import *
import unittest
class test_prog(unittest.TestCase):
    # Test Case function to check  if the given matrix is singular or not
    def test(self):
        
# TEST CASES PASSED(Singular matrix => matrix=0 )
        self.assertEqual(is_singular(matrix=[[2, -3, 4], [2, -3, 4], [0, -1, 1]]),0)
#        self.assertEqual(is_singular(matrix=[[3, 8, 1], [-4, 1, 1], [-4, 1, 1]]),0)

# TEST CASES FAILED(Non-Singular matrix)
#        self.assertEqual(is_singular(matrix=[[1, 3, 8], [3, 3, 7], [8, 5, 1]]),0)
#        self.assertEqual(is_singular(matrix=[[51, 4, 1], [67, 3, 4], [5, 6, 1]]),0)

if __name__ == '__main__':
    unittest.main()