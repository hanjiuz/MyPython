#lambda - anonymous function
(lambda x, y: x+y)(3,7)

numbers = [0, 1, 2, 3, 4, 5]
mapped_numbers = map(lambda n:n*n, numbers)
for i in mapped_numbers:
	print(i)


#student_tuples
student_tuples = [
    ('James', 'A', 40),
    ('Frank', 'C', 50),
    ('Rick', 'B', 45),
]

#sort by age
print(sorted(student_tuples, key=lambda student: student[2], reverse=True))

#student_objects
class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def __repr__(self):
		return repr((self.name, self.grade, self.age))

student_objects = [
    Student('James', 'A', 40),
    Student('Frank', 'C', 50),
    Student('Rick', 'B', 45),
]

#sort by name
print(sorted(student_objects, key=lambda student: student.name))


#use operator module methods to replace lambda
from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('name')))

#multiple level sorting
print(sorted(student_tuples, key=itemgetter(2, 1)))
print(sorted(student_objects, key=attrgetter('age', 'grade')))

