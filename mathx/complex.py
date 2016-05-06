class Complex(object):
    

    def __init__(self, real, imaginary):
        
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return '<complex: ({}, {}i)>'.format(self.real, self.imaginary)


    def __str__(self):

        return ('({0:.2f}, {0:.2f}i)'.format(round (self.real, self.imaginary, 2)))

    def __add__(self, other):

        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary

        return Complex(real, imaginary)

    def __sub__(self, other):

        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary

        return Complex(real, imaginary)

    def __mul__(self, other):

        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real

        return Complex(real, imaginary)

    def __div__(self, other):

        j = float(other.real ** 2 + other.imaginary ** 2)
        z = self * Complex(other.real, -other.imaginary)
        real = z.real / j
        imaginary = z.imaginary / j

        return Complex(real, imaginary)