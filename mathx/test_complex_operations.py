import unittest
from complex import Complex
a = Complex(1, 2)
b = Complex(2, 1)
d = Complex(3, 4)

class ComplexOperationsTestCase(unittest.TestCase):

        def test_sum_of_complex_numbers(self):
            c = a + b
            self.assertEqual( str(c), ('(3, 3i)'))
            c = a + b + d
            self.assertEqual( str(c), ('(6, 7i)'))

        def test_difference_of_complex_numbers(self):
            c = a - b
            self.assertEqual(str(c), ('(-1, 1i)'))
            c = a - d
            self.assertEqual(str(c), ('(-2, -2i)'))


        def test_multiplication_of_complex_numbers(self):
            c = a * b
            self.assertEqual(str(c), ('(0, 5i)'))

        def test_division_of_complex_numbers(self):
            c = a / b
            self.assertEqual(str(c), ('(0.8, 0.6i)'))

if __name__ == '__main__':
    unittest.main()






	

	
  		
  		
  		
  		
  		
