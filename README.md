[![Build Status](https://travis-ci.org/maureengithu/bc-7-mowplex.svg?branch=master)](https://travis-ci.org/maureengithu/bc-7-mowplex)

 **BC-7-MOWPLEX**
 -----------------

**Prelude**:

*Assumption*: 
ou can't take the square root of a negative number.

*Fact*:
You can take the square root of a negative number, but it involves using a new number to do it. This new number is commonly called "i", standing for "imaginary".

*Definition of complex number*:
A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, that satisfies the equation i<sup>2</sup> = −1.

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

* mathx: A complex numbers library that will perform operations of addition, subtraction, multiplication and division on complex numbers.

* mowplex: A command line program that allows users to  minimize complexity by using short commands to perfom operations on complex numbers

**Installation and setup**
  -----------------------
```shell
$ git clone https://github.com/maureengithu/bc-7-mowplex.git
$ cd bc-7-mowplex
$ python
>>> import complex
...
```

**Tests**
  -----

The tests have been written using python's TestCase class.
The program is intergrated to Travis CI which automatically detects when a commit has been made and pushed to the GitHub repository, and each time this happens, it will try to build the project and run tests. For intergration steps visit https://travis-ci.com/getting_started

Ensure that you have installed pip on your cmd for travis to function as intended.

```shell
$ pip install nose
$ nosetests
```

If the tests are successful, they will complete without failures or errors.

Output Example
```shell
....
----------------------------------------------------------------------
Ran 4 tests in 0.015s

OK
```