def are_valid_groups(student_numbers, groups) -> bool:
	boolean = False
	for n in student_numbers:
		for i in groups:
			if n in i:
				boolean = True
				
		if not boolean:
			return False
				
	return True
