def fizz_buzz(arg):
	value = []
	if (arg%3==0 or arg%5==0):
		if arg%3==0:
			value.append('Fizz')
		if arg%5==0:
			value.append('Buzz')
		return ''.join(value)
	else:
		return arg