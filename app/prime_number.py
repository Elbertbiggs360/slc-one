import math

class PrimeNumber(object):

	def compute_prime_numbers(given_argument):
		"""TODO: Create function to determine prime numbers between 0 and given_argument"""
		if isinstance(given_argument, int) is False:
			raise TypeError("The argument you passed is not an integer")
		else:
			if given_argument<3:
				raise ValueError("Input Number Greater Than 2")
			else:
				prime_list =[]
				prime_list.append(2)
				nextPrime = 3

				while nextPrime<given_argument:
					isPrime = True
					sqrt_value = math.sqrt(nextPrime)

					sample_range = [i for i in prime_list if i <= sqrt_value]
					
					for i in sample_range:
						if nextPrime%i==0:
							isPrime = False
							break
					if isPrime:
						prime_list.append(nextPrime)

					nextPrime +=2

				return prime_list


									