def MissingNumber(array_one, array_two):
	if isinstance(array_one, list) and isinstance(array_two, list):
		if all(i>=0 and isinstance(i, int) for i in array_one) and all(i>0 and isinstance(i, int) for i in array_two):
			set_one = set(array_one)
			set_two = set(array_two)
			return (set_one ^ set_two)
		else:
			raise ValueError("Only Integers needed")
	else:
		raise TypeError('Only arrays')

MissingNumber([2,3,4],[2,3])