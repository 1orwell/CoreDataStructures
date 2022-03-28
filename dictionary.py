student_grades = {
    "Jack" : [85, 90],
    "Jill" : [95, 60]
}

def get_grades(name):
    return student_grades.get(name, [])

def get_or_assign(name):
    return student_grades.setdefault(name, [100,100])

print(get_grades("Jack"))
print(get_or_assign("Jlck"))

print(student_grades)