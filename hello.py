print(("Hello " + "World!\n") * 10)


names = ("James", "Elaine", "Frank", "Rick", "Steve")
print(names)

for name in names:
	print(name)

for i in range(len(names)):
	print("names #" + str(i) + " : " + names[i])

for i, name in enumerate(names):
	print("names #" + str(i) + " : " + name)


#three operators expression
len = 5 if len(names) == 5 else 0
print("three operators expression: len=" + str(len))

for i in [0,1,2,3,4,5]:
	if i > 3:
		print(str(i))
	else:
		print(str(i+3))
else:
	print("finish for...else...")



#列表推导式 list derivation expression
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [i*i for i in numbers]
print(numbers)
print(squares)


def get_square(number):
	for n in range(number):
		yield(pow(n,2))

sss = repr(get_square(100))
print(sss)

for item in get_square(100):
	print(item)


