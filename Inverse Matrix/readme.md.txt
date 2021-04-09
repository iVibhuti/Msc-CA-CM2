Assignment 1
Table of contents
Introduction
Requirements
Setup
Input File
Output File
#Introduction
The program takes in a input and calculates the determinant of the given matrix. Based on the determinant it finds whether the given input is singular or non-singular.
Input to the program is given in input.txt but if user wishes to provide their own matrix they can edit the input.txt file.

#Requirements
Python3
To install python visit this link: (https://www.python.org/).

#Setup
Download and place the files in a directory.
Ensure that Input.txt and IsMatrixSingular.py are in same directory.
If not, Paste appropriate path of Input.txt in InputFile[] section.
If You wish to make changes to Input.txt Follow the same format.

🔹Input File
Input.txt file follows a comma seperated structure.
Each line represents row in the matrix.
Each line has 3 values seperated by comma which represents columns.

Explanation-FAQ
What is checkerBoard list in the program?
checkerBoard list is used to apply + - + pattern to all values of first row. It is required to calculate determinant.

What is getMatrixOfMinor method?
It is a method used to find minors of all corresponding values in the 0th row of given input which is required to calculate the determinant of input.

What is getDeterminant method?
The method takes 2X2 matrix as input and returns the determinant of that matrix by using ad - bc where, [[a ,b],[c ,d]].

What is calculateDeterminant method?
returns a determinant of 3X3 matrix by multiplying each value in the 0th row with its own corresponding checkerBoard pattern. Then multiplying that value to its corresponding minor and then adding that value to solution variable which is our determinant.

What is isSingular method?
returns True if determinant is 0, else it returns False.

What is getInputFromFile?
It takes a file name and converts the file into proper 3X3 matrix input. The input is converted from comma seperated structure to a 3X3 matrix of type list.

What is instructions section?
Its simply a list of statements to call all the functions in the program.