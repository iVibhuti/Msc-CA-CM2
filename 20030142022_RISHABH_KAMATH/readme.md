A Unit TestCase to check a Singular Matrix
Unit Testing is the first stage of software testing method in which the smallest testable unit of

a software are tested. It allows each unit of the software to be validated with respect to its expected design performance.
unittest.TestCase is used to create test cases by subclassing it.
To execute the test cases:

(1) Uncomment the pass regions for test cases that satisfy the condition of singular matrix.

(2) comment the pass regions and uncomment the FAIL regions for test cases that does not satisfy the condition of singular matrix.
Test Outcomes Possible :

(1) OK – This means that all the tests are passed. (2) FAIL – This means that the test did not pass and an AssertionError exception is raised.
if name == 'main':

unittest.main()    
