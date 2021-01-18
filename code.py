def are_valid_groups(student_numbers) -> bool:
	for group in groups:
		inside = False
		for number in student_numbers:
			if number in group:
				inside = True			
		if not inside:
			return False
	return True

	random stuff
