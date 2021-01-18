def is_valid_groups(students, groups):
    for i in groups:
        for j in i:
            if(j in students):
                students.remove(j)
    if not students:
        return True
    else:
        return False
        
print(is_valid_groups([1,2,3,4], [[1,2], [3], [5]]))
