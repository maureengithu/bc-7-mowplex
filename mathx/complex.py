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

    def __repr__(self):
        return '<complex: ({}, {}i)>'.format(self.real, self.imaginary)


    def __str__(self):

        # if self.real == '' or self.imaginary == '':
        #     return 'Input a real and imaginary value'
        return '({}, {}i)'.format(self.real, self.imaginary)

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