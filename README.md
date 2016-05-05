  **BC-7-MOWPLEX**
  -----------------

**Prelude**:

*Assumption*: 
You can't take the square root of a negative number.

*Fact*:
You can take the square root of a negative number, but it involves using a new number to do it. This new number is commonly called "i", standing for "imaginary".

*Definition of complex number*:
A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, that satisfies the equation i**2 = −1.

**Breakdown**:
  ----------

*Addition*

It's all just combining like terms. First combine the real units, then the imaginary units.

*Subtraction*

Subtraction is basically the same, but it does require you to be careful with your negative signs.

*Multiplication*

Here are the steps required for Multiplying Complex Numbers:

* Step 1:	Distribute to remove the parenthesis.
* Step 2 : Simplify the powers of i, specifically remember that i2 = –1.
* Step 3 : Combine like terms, that is, combine real numbers with real numbers and imaginary numbers with imaginary numbers.

*Division*

Here are the steps required to divide complex numbers:

* Step 1:	To divide complex numbers, you must multiply by the conjugate. To find the conjugate of a complex number all you have to do is    change the sign between the two terms in the denominator.
* Step 2:	Distribute in both the numerator and denominator to remove the parenthesis.
* Step 3:	Simplify the powers of i, specifically remember that i2 = –1.
* Step 4:	Combine like terms in both the numerator and denominator, that is, combine real numbers with real numbers and imaginary numbers with imaginary numbers.
* Step 5:	Write you answer in the form a + bi.
* Step 6:	Reduce your answer if you can.

**Back End Dependencies**
  ----------------------
This console application's functionality depends on two Python packages including;
*mathx- A complex numbers library that will perform operations of addition, subtraction, multiplication and division on complex numbers.
*mowplex- A command line program that allows users to  minimize complexity by using short commands to perfom operations on complex numbers

**Front End Dependencies**
  -----------------------

termcolor 1.1.0- ANSII Color formatting for output in terminal

**Installation and setup**
  -----------------------

*Navigate to a directory of choice on terminal.

*Clone this repository on that directory - https://github.com/maureengithu/bc-7-mowplex.git

*Navigate to the repo's folder on your terminal

*cd /bc-7-mowplex

*Import the packages and run the app.

**Tests**
  -----

The tests have been written using python's TestCase class.
The program is intergrated to Travis CI which automatically detects when a commit has been made and pushed to the GitHub repository, and each time this happens, it will try to build the project and run tests.
If the tests are successful, they will complete without failures or errors.

Example
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.015s

OK
```