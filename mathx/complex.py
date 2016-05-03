import math 

class Complex(object):
	'''
	A complex numbers class function that will
	perform operations on complex numbers such as;
		-addition
		-subtraction
		-multiplication
		-division
	'''

	def __init__(self, real, imaginary):
		#Takes in two or more real numbers
		#Takes in two or more complex numbers
		
		self.real = real
		self.imaginary = imaginary

		if isinstance(other, (float,int)):

			other = Complex(other)

		elif not (hasattr(other, 'real') and hasattr(other, 'imaginary')):

			raise TypeError('other must have real and imaginary attr.')

	def __add__(self, other):
		#adds two or more complex numbers

		real = self.real + other.real
		imaginary = self.imaginary + other.imaginary

		return Complex(real, imaginary)

	def __sub__(self, other):
		#subtracts two or more complex numbers

		real = self.real - other.real
		imaginary = self.imaginary - other.imaginary

		return Complex(real, imaginary)

	def __mul__(self, other):
		#multiplies two or more complex numbers

		real = self.real * other.real - self.imaginary * other.imaginary
		imaginary = self.real * other.imaginary + self.imaginary * other.real

		return Complex(real, imaginary)

	def __div__(self, other):
		#divides two or more complex numbers

		j = float(other.real ** 2 + other.imaginary ** 2)
		z = self * Complex(other.real, -other.imaginary)
		real = z.real / j
		imaginary = z.imaginary / j

		return Complex(real, imaginary)