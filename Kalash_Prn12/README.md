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
This program is to check test cases for checking **Matrix Singularity** using **unittest** in **Python**.
***
Unit testing:
-It is one of the first stages in **Software testing** before the whole software is tested
-It is used for testing **individual units** and **components** of a software program or code
-This type of testing is done during the **development of a software program** to avoid errors later
-A unit test can have **multiple test cases** to check different aspects of a code
-The purpose of unit testing is to iron out **exceptional cases** and get **desired output** from the code
-In python **unittest.TestCase** is used to create test cases by sub classing it
***
### Requirements
Requirements For running this program
***
Required specifications and software: 
- Python version **3** or above as the code is using python3 syntax and unittest was first introduced in python version 2.1
- **1mb** or above of storage space
***
### Setup
Setup the files before proceeding
***
Setup instructions:
- Save the files in a folder location of your choice and make sure files are placed in **same folder**
- Open the command line and ensure **python** is working by executing `python --version` on the command line and check if appropriate python version is installed
***
### Execution
Here we see how to execute the code and different test cases
***
Execution instructions:
- In the file **test_singularity.py** the class **test_singularity** is the class which extends the unittest.TestCase class
- In this class two test cases are setup i.e **test_pass** and **test_fail**
- Two test cases can be executed **together** or **separately**:
    - To execute the test cases that are **singular matrix** and satisfy the test case comment the **test_fail** test case section
    - To execute the test cases that are **not singular matrix** and don’t satisfy the test cases comment the **test_pass** test case section
- Now, open the **command terminal** and navigate to the folder where the code files are saved
- Execute the code by using the commands:
    - `python test_singularity.py`: This command can be used for normal execution if the code has the below function which allows the tests to run just by executing the python code
    ```python
    if __name__ == '__main__':
        unittest.main() 
    ``` 
    - `python -m unittest -v test_singularity.py`: This command can be used for executing the test cases with or without including main in the code and outputs more detailed information on the test cases that have been executed and their result on the terminal
***
### Output
Here we will see the output of the executed unit test cases
***
- Two possibilities for output are "OK" and "FAIL":
    - OK: Indicates that the unit test cases have passed
    - FAIL: Indicates that the unit test cases did not pass and an AssertionError exception occurs and shows the error on which line the test cases did not pass on command prompt
- Output image where both test cases are executed
![Output image of pass and fail test cases](https://github.com/iVibhuti/Msc-CA-CM2/blob/64e12ab3da590392269b23f5fee2ddce181a8ece/Kalash_Prn12/screenshots/PassFail.png)

- Output image where `test_pass` test cases are executed
![Output image of pass test cases](https://github.com/iVibhuti/Msc-CA-CM2/blob/64e12ab3da590392269b23f5fee2ddce181a8ece/Kalash_Prn12/screenshots/Pass.png)

- Output image where `test_fail` cases are executed
![Output image of fail test cases](https://github.com/iVibhuti/Msc-CA-CM2/blob/64e12ab3da590392269b23f5fee2ddce181a8ece/Kalash_Prn12/screenshots/Fail.png)

***
## END of README file
***
