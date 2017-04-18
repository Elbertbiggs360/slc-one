import unittest
from app.prime_number import PrimeNumber
import math

class PrimeNumberTest(unittest.TestCase):
	
	def setUp(self):
		self.prime_number = Prime_number()
		self.arg_limit = 32
        self.sample_prime = [2,3,5,7,911,13,17,19,23,29,31]
        self.sample_prime_length = 11

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

	def test_generate_prime_numbers_returns_all_prime_numbers_less_than_arg(self):
        self.assertEqual(self.sample_prime_length, len(self.prime_number.compute_prime_numbers(self.arg_limit)))

	def test_function_returns_prime_numbers(self):
		isPrime = True
        for x in self.prime_number.compute_prime_numbers(self.arg_limit):
            sqrt_value = sqrt(x)
            sample_range = [i for i in self.sample_prime if i <= sqrt_value]
            for y in sample_range:
                if x%y == 0:
                    isPrime = False
                    break
        self.assertTrue(isPrime)


if __name__ = '__main__':
	unittest.main()