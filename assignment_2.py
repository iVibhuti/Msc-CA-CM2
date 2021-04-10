# Python code to check if the test cases are singular or non singular using unittest
from assignment_1 import *
import unittest
import mat_check as match
  
class test_sing(unittest.TestCase):
    
    def test_mat(self):
        self.assertEqual(match.t_sing([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),0) #PASS
        #self.assertEqual(match.t_sing([[34, 45, 4], [0, 0, 0], [7, 4, -54]]),0)

    def test_false(self):
        self.assertEqual(match.t_sing([[78, 45, 4], [0, 0, 0], [7, 4, -54]]),1) #PASS
        
#Code to execute the test Case
if __name__ == '__main__':
    unittest.main()
