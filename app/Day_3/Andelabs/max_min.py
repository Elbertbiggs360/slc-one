def find_max_min(arg):
	value_list = sorted(arg)
	if value_list[0]==value_list[len(arg)-1]:
		return [len(arg)]
	else:
		return [value_list[0], value_list[len(arg)-1]]