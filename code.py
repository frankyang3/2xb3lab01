def are_valid_groups(student_numbers, groups):
	for number in student_numbers:
		inside = False
		for group in groups:
			if number in group:
				inside = True			
		if not inside:
			return False
	return True
