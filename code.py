def are_valid_groups(student_numbers, groups) -> bool:
	for n in student_numbers:
		for i in groups:
			if not n in i:
				return False
				
	return True
