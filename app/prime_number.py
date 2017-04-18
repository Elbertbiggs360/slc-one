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
				prime_numbers = [2]
				for i in range(given_argument): #n
					if i>131:
						for n in range(int(math.sqrt(i)) ):#loop through all values between 0 and the square root
							if n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0:
								continue
							else:#for every prime number
								if i%n!=0 and i is not 1:#check if i is not a multiple of the prime number n
									prime_numbers.append(i) #add i to prime numbers if it is not
					elif given_argument>12:
						if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0:
							continue
						else:
							if i is not 1:
								prime_numbers.append(i)
					else:
						break
				return prime_numbers


									