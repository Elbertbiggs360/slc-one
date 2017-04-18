import unittest

class PrimeNumberTest(unittest.TestCase):

	def test_function_returns_integers(self):
		"""Check that the function only returns integers """
		prime_number = prime_number()
		result = prime_number.compute_prime_numbers(10)
		test_value = False
		if isinstance(result, int):
		if all(isinstance(result[i], int) for i in result)
			test_value = True
		else:
			test_value = False
		self.assertTrue(test_value)