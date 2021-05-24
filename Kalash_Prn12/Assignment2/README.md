# Matrix Singularity Test Case Program 
***
Readme file for a test program for checking **Matrix singularity** using **unittest** in **Python**
***

## Table of Contents
1. [General Info](#General-Info)
2. [Requirements](#Requirements)
3. [Setup](#Setup)
4. [Execution](#Execution)
5. [Output](#Output)
***
### General-Info
This program is to calculate, display and check the **Factors of a Matrix** using **SVD Method** in **Python**.
***
In linear algebra, the singular value decomposition (SVD) is a factorization of a real or complex matrix that generalizes the eigen decomposition, which only exists for square normal matrices, to any m* n}m* n matrix via an extension of the polar decomposition.

   Specifically, the singular value decomposition of an m* n}m* n complex matrix M is a factorization of the form UΣ V^{t}, where U is an m x m complex unitary matrix, Σ is an m x n rectangular diagonal matrix with non-negative real numbers on the diagonal, and V is an n x n complex unitary matrix. If M is real, U and V can also be guaranteed to be real orthogonal matrices. In such contexts, the SVD is often denoted UΣV^{T}.

***
### Requirements
Requirements For running this program
***
Required specifications and software: 
- Python version **3.5** or above
- **Numpy** and **SymPy** Libraries
- **1mb** or above of storage space
***
### Setup
Setup the files before proceeding
***
Setup instructions:
- Save the files in a folder named **code** in location of your choice and make sure files are placed in **same folder**
- Open the command line and ensure **python** is working by executing `python --version` on the command line and check if appropriate python version is installed
***
### Execution
Here we see how to execute the code and get the factors of matrix using SVD
***
Execution instructions:
- In the file **input.txt** enter the matrix for which you wish to see the U,Σ,Vt factors
- In the file **GetSvd.py** the class **getSvdFactors** is the function which gets the Factors
- In this class two test cases are setup i.e **test_pass** and **test_fail**

- Now, open the **command terminal** and navigate to the folder where the code files are saved
- Execute the code by using the commands:
    - `python main.py`: This command can be used for normal execution of the code and the function to get values is as follows getSVD
    ```python
        getSvd(matrix)
    ``` 
    - `python alternate.py`: This command is an alterante file to find SVD of a matrix for certain matrix
***
### Output
Here we will see the output of the executed fucntion and see the different factors i.e U,Σ,V^{T}
***

- Output or matrix [[ 5, 5],[ -1, 7]]
![Output image of pass and fail test cases](https://github.com/iVibhuti/Msc-CA-CM2/blob/main/Kalash_Prn12/Assignment2/screenshots/Screenshot%20(301).png)


***
## END of readme file
***
