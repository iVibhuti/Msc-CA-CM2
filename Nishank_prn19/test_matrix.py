import unittest
import matsingularity as ms
  
class test_matrix(unittest.TestCase):

    #passed test case
    def t_pass(self):
        self.assertEqual(ms.Sing([[1, 4, 1], [1, 6, 1], [1, 7, 1]]),0) #CASE1
        
    #failed test cases
    #def t_fail(self):
        #self.assertEqual(ms.Sing([[4, 3, 8], [1, 3, 7], [6, 5, 3]]),0) #CASE1
        
          
#execution
if __name__ == '__main__':
    unittest.main()
