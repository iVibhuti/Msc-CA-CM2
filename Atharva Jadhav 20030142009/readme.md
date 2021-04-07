# Computational methods assignment
## Table of contents
1. [General info](#general-info)
2. [Requirements](#requirements)
3. [How to setup](#how-to-setup)
4. [Input file structure](#input-file-structure)
5. [Explanation-FAQ](#explanation-faq)

### General info
***
The program takes in a input and calculates the determinant of the given matrix. Based on the determinant it finds whether the given input is singular or non-singular.

Input to the program is given in input.txt but if user wishes to provide their own matrix they can edit the input.txt file.

### Requirements
***
> Ensure that you have python (any version above 3) installed in the environment.
> To install python in your OS, goto- (https://www.python.org/).

### How to setup
***
> Download and place the files in a directory.
> Ensure that input.txt and invertible.py are in same directory.
> If user wishes to make changes to input.txt they can view (#input-file-structure) section.

### Input file structure
***
> input.txt file is simply a comma seperated structure.
> each line represents row in the matrix.
> each line has 3 values seperated by comma which represents columns.

Note: As of version 1.0, the program only supports the input of 3X3 matrix (3 rows & 3 colmuns).

### Explanation-FAQ
***
1. **What is checkerBoard list in the program?**
> checkerBoard list is used to apply + - + pattern to all values of first row. It is required to calculate determinant.

2. **What is getMatrixOfMinor method?**
> It is a method used to find minors of all corresponding values in the 0th row of given input which is required to calculate the determinant of input.

3. **What is getDeterminant method?**
> The method takes 2X2 matrix as input and returns the determinant of that matrix by using ad - bc where, [[a ,b],[c ,d]].

4. **What is calculateDeterminant method?**
> returns a determinant of 3X3 matrix by multiplying each value in the 0th row with its own corresponding checkerBoard pattern. Then multiplying that value to its corresponding minor and then adding that value to solution variable which is our determinant.

5. **What is isSingular method?**
> returns True if determinant is 0, else it returns False.

6. **What is getInputFromFile?**
> It takes a file name and converts the file into proper 3X3 matrix input. The input is converted from comma seperated structure to a 3X3 matrix of type list.

7. **What is instructions section?**
> Its simply a list of statements to call all the functions in the program.
