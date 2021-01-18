def is_valid_groups(student_numbers, groups):
	for group in groups:
		inside = False
		for number in student_numbers:
			if number in group:
				inside = True			
		if not inside:
			return False
	return True

print(is_valid_groups([1,2,3,4], [[1,2], [3], [4]]))
