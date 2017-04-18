import unittest
from app.prime_number import PrimeNumber
import math

class PrimeNumberTest(unittest.TestCase):
	
	def setUp(self):
		self.prime_number = Prime_number()

	def test_function_returns_integers(self):
		"""Check that the function only returns integers """
		result = self.prime_number.compute_prime_numbers(10)
		test_value = False
		if all(isinstance(result[i], int) for i in result)
			test_value = True
		else:
			test_value = False
		self.assertTrue(test_value)

	def test_function_returns_list_of_values(self):
		self.assertIsInstance(self.prime_number.compute_prime_numbers(15), list)

	def test_function_returns_value_error_if_arg_not_int(self):
		self.assertRaises(TypeError, self.prime_number.compute_prime_numbers(), 'two' )

	def test_function_returns_value_error_if_arg_less_than_three(self):
		self.assertRaises(ValueError('Input Number Greater than 2'), self.prime_number.compute_prime_numbers(), 1)

	def test_function_returns_prime_numbers(self):
		result = self.prime_number.compute_prime_numbers(15)
		test_value = False
		for i in result:
			for n in len(round(math.sqrt(i)))
				if n%2!=0 or n%3!=0 or n%5!=0:
					if i%n==0:
						test_value = False
					else:
						test_value = True
		
		self.assertTrue(test_value)


if __name__ = '__main__':
	unittest.main()