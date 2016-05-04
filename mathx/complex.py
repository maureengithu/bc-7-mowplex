#import math 

class Complex(object):
    '''
    A complex numbers class that will
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

    def __str__(self):
        return '({}, {}i)'.format(self.real, self.imaginary)



    def __add__(self, other):
        #adds two or more complex numbers

        if isinstance(other, (float,int)):

            other = Complex(other)

        # elif not (hasattr(other, 'real') and

        #           hasattr(other, 'imag')):

        #     raise TypeError('other must have real and imag attr.')

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

C = map(float, raw_input().split())
D = map(float, raw_input().split())
j = ComplexNo(*C)
z = ComplexNo(*D)
final = [j+z, j-z, j*z, j/z]
print '\n'.join(map(str, final))
