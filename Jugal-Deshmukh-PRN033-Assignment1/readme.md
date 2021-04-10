# Computational Methods Check Singular Matrix Assignment 

## Files and packages needed for execution
* checkmatrixsingularity.py 
* test_singular_matrix.py 
* unittest (inbuilt python package)

## Files Information

* checkmatrixsingularity python file contains the main python code for calculating the cofactor and determinant of a matrix. After that it also checks whether the matrix is singular or non-singular in nature.

* test_singular_matrix python file is the testcase file that contains a list of passed and failed test cases for the checkmatrixsingularity python file. 

## What is unittest module?
```Unit Testing is the first stage of software testing method in which the smallest testable unit of a software is tested. It allows each individual unit of the program to be validated with regard to its expected design performance. ```

```The unittest.TestCase parameter in the program is used to create various test cases by subclassing it. ```

```So basically the unittest module provides a rich set of tools for constructing and running various tests or testcases.```


## Why is unittest.main() required?
if __name__ == '__main__':```

    unittest.main()
    is required in order to run the testcases using unitttest module.

## What is an AssertionError?
Like many programming languages, Python includes a built-in assert statement that allows you to create simple debug message outputs based on simple logical assertions. When such an assert statement fails (i.e. returns a False-y value), an AssertionError is raised.

## Program Execution steps

1. Go to the python files location folder in your system using the command prompt.

2. To check passed test cases, uncomment the **test_pass(self)** function from the **test_singular_matrix.py** file. Make sure the **test_fail(self)** function is commented.

3. To check failed test cases, uncomment the **test_fail(self)** function from the **test_singular_matrix.py** file. Make sure the **test_pass(self)** is commented.

4. Type **python -m unittest -v test_singular_matrix.py** to run the test case file. This will provide the detailed information regarding passed and failed test cases of the program.

## Test Case Outcomes

1. **ok** - If this outcome appears then it means that all the test cases have met the singular matrix requirements and have passed.

2. **FAIL** - If this outcome appears then it means that the test cases have not met the singular matrix requirement and an **AssertionError** has occurred. 




