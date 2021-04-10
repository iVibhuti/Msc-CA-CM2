# Python code to check ytest cases for singular or not matrix using unittest

import unittest
import matrix_check_singularity as mcs
  
class test_singularity(unittest.TestCase):
    
    def test_matrix(self):
        self.assertEqual(mcs.is_singular([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),0) #PASS
        self.assertEqual(mcs.is_singular([[34, 45, 4], [0, 0, 0], [7, 4, -54]]),0)

    def test_fail(self):
        self.assertEqual(mcs.is_singular([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),1) #PASS
        
#To Execute The Test Case
if __name__ == '__main__':
    unittest.main()
