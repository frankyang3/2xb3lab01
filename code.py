<<<<<<< HEAD
def are_valid_groups(student_numbers, groups):
	
	for number in student_numbers:
		inside = False
		for group in groups:
			if number in group:
				inside = True
				
		if not inside:
			return False
				
	return True
=======
def are_valid_groups(student_numbers, groups) -> bool:

        for number in student_numbers:
                inside = False
                for group in groups:
                        if number in group:
                                inside = True

                if not inside:
                        return False

        return True
>>>>>>> 2e0a74a3fa0481d880be714013847a435af489a2
