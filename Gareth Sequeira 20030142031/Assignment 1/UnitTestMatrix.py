#Import Files
from IsMatrixSingular import *
import unittest

#Create Class for Testing
class TestNonSingular(unittest.TestCase):

    def TestMatrix(self):


#Test If MAtrix is Non-Singular
#CASE 1: 2x2 Matrix
##  self.assertEqual(checkNonSingular(Matrix=[[1, 2], [3, 2]]),0)
#PASS

#CASE 2: 3x3 Matrix 
##  self.assertEqual(checkNonSingular(Matrix=[[2, 6, 1], [-3, 0, 5], [-7, 5, 4]]),0)
#PASS


#Test If Matrix is Singular If Fails, Then Singular
#CASE 1: 2x2 Matrix
##  self.assertEqual(checkNonSingular(Matrix=[[1, 2], [1, 2]]),0)
#FAIL

#CASE 2: 2x2 Matrix 
##  self.assertEqual(checkNonSingular(Matrix=[[3, 8, 1], [-4, 1, 1], [-4, 1, 1]]),0)
#FAIL


#MainClass
if __name__ == '__main__':
    unittest.main()