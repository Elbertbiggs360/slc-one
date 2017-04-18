import math

class PrimeNumber(object):

	def compute_prime_numbers(self, argument):
		"""TODO: Create function to determine prime numbers between 0 and argument"""
		if isinstance(argument, int) is False:
			raise TypeError("The argument you passed is not an integer")
		else:
			if argument<3:
				raise ValueError("Input Number Greater Than 2")
			else:
				prime_list =[]
				prime_list.append(2)
				next_prime = 3

				while next_prime<argument:
					is_prime = True
					sqrt_value = math.sqrt(next_prime)

					sample_range = [i for i in prime_list if i <= sqrt_value]#(log(n)
					
					for i in sample_range:
						if next_prime%i==0:
							is_prime = False
							break
					if is_prime:
						prime_list.append(next_prime)

					next_prime +=2#(n/2)

				return prime_list


prime_number = PrimeNumber()
print prime_number.compute_prime_numbers(9)


									