# Python code to check ytest cases for singular or not matrix using unittest

import unittest
import mat_check as mc
  
class test_sing(unittest.TestCase):
    
    def test_mat(self):
        self.assertEqual(mc.t_sing([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),0) #PASS
        #self.assertEqual(mc.t_sing([[34, 45, 4], [0, 0, 0], [7, 4, -54]]),0)

    def test_false(self):
        self.assertEqual(mc.t_sing([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),1) #PASS
        
#To Execute The Test Case
if __name__ == '__main__':
    unittest.main()
