# Python code to check ytest cases for singular or not matrix using unittest

#import required libraries and code
import unittest
import cal_determinant as cd

#Test case class extending unittest.TestCase
class test_singularity(unittest.TestCase):

    #Test case to check if given matrix are not singular
    def test_pass(self):
        self.assertEqual(cd.check_singular([[0, 0, 0], [45, 50, 30], [17, 4, -11]]),0)
        self.assertEqual(cd.check_singular([[41, 34, 54], [0, 0, 0], [43, 5, 34]]),0)
        self.assertEqual(cd.check_singular([[2, 4, 6], [2, 0, 2], [6, 8, 14]]),0)
        self.assertEqual(cd.check_singular([[2, 2], [2, 2]]),0)

    #Test case to check if given matrix are not singular
    def test_fail(self):
        self.assertEqual(cd.check_singular([[24, 235, 5], [0, 1, 0], [7, 4, -7]]),0)
        self.assertEqual(cd.check_singular([[25, 3, 7], [2, 0, 5], [7, 1, 4]]),0)
        self.assertEqual(cd.check_singular([[78, 45], [5, 5]]),0)

        
#To Execute The Test Case
if __name__ == '__main__':
    unittest.main()
