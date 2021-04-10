import unittest
import check_singular as cs
  
class test_singular_matrix(unittest.TestCase):

    #This function contains all the passed test cases of singular matrix
    def test_pass(self):
        self.assertEqual(cs.check_singular([[78, 45, 4], [0, 0, 0], [7, 4, -54]]
,0) #PASS CASE1
        self.assertEqual(cs.check_singular([[1,-2],[-3, 6]]),0) #PASS CASE2
    
    #This function contains all the failed test cases of singular matrix
    #Uncomment to run the below test case function
    def test_fail(self):
        self.assertEqual(cms.check_singular([[1,0],[0, 1]]),0) #FAIL CASE1
        self.assertEqual(cms.check_singular([[34, 45],[6, 5]]),0) #FAIL CASE2
          
          
#To Execute The Test Case
if __name__ == '__main__':
    unittest.main()