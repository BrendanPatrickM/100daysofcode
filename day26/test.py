import random
names = ['Alex', 'Beth', 'Caroline', "Dave", 'Eleanor', 'Freddie']

# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

student_scores = {name: random.randint(0, 100) for name in names}
# new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
passed_students = {student: score for (student, score) in student_scores.items() if score > 74}

print(student_scores)
print(passed_students)
