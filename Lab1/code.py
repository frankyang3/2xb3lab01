def are_valid_groups(student_numbers, groups):
	x = []
	for group in groups:
		inside = False
		for number in student_numbers:
			if number in group:
				inside = True
		if len(group) != 2 and len(group) != 3:
			return False
		if not inside:
			return False
		for y in group:
			x.append(y)
	if len(x) != len(set(x)):
		return False
	if len(student_numbers) != len(set(student_numbers)):
		return False
	return True

print(are_valid_groups([1,2,3,4,5,6], [[1,2], [3,4], [5,6]]))
