def find_missing(array_one, array_two):
	if isinstance(array_one, list) and isinstance(array_two, list):
		if all(i>=0 and isinstance(i, int) for i in array_one) and all(i>0 and isinstance(i, int) for i in array_two):
			missing_values = list(set(array_one)^set(array_two))
			if len(missing_values) is 0:
				return 0 
			elif len(missing_values) is 1:
				return missing_values[0]
			else:
				return missing_values
		else:
			raise ValueError("Only Integers needed")
	else:
		raise TypeError('Only arrays')

find_missing([2,3,4],[2,3])