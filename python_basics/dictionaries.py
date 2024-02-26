
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

student['phone'] = '555-5555' #to add new keys
student.update({'name': 'Jane', 'age': 26, 'sex': 'woman'}) #Updating existing keys and adding new ones at once

print(student)
print(student['name'])
print(student.get('adress', 'Not Found')) #Works to get specified message for non-exist keys rather than an error

del student['sex']

print(student)

age = student.pop('age')

print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)



