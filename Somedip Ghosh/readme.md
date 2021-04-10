# A unittest to check wheather matirx is singular or not?
## What is Python Unittest?
Python Unittest is a Python Unit-Testing framework. Inspired by JUnit, it is much like the unit testing frameworks we have with other languages.
### Here are some features it supports-
. Test automation . Sharing setup and shutdown code for tests . Aggregating tests into collections . Independence of tests from the framework
1.	Concepts in an object-oriented way for Python Unittest . Test fixture- the preparation necessary to carry out test(s) and related cleanup actions. . Test case- the individual unit of testing. . A Test suite- collection of test cases, test suites, or both. . Test runner- component for organizing the execution of tests and for delivering the outcome to the user.
### How Python Unittest Works?
So we’ve seen this Unit Testing with Python works without much effort. But how does this happen behind the scenes?
1.	Subclassing unittest.TestCase
2.	Python Unittest Assert Methods Now, let’s take a look at what methods we can call within Unit testing with Python:
. assertEqual()- Tests that the two arguments are equal in value. . assertNotEqual()- Tests that the two arguments are unequal in value. . assertTrue()- Tests that the argument has a Boolean value of True. . assertFalse()- Tests that the argument has a Boolean value of False. . assertIs()- Tests that the arguments evaluate to the same object.
3.	unittest.main()
This delivers a command-line interface to the test script. The output suggests whether the tests ran okay or failed.
### Tests That Fail in Python Unittesting
What happens if a test fails? To make this happen, we refer to a string variable that doesn’t already exist.
### Outcomes Possible :
There are three types of possible test outcomes :
OK – This means that all the tests are passed. FAIL – This means that the test did not pass and an AssertionError exception is raised. ERROR – This means that the test raises an exception other than AssertionError
### if name == 'main':

unittest.main()    

allows us to run all the tests just by executing the file.
