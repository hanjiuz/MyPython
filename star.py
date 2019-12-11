# star * for multiple args
def multi_sum(*args):
    result = 0
    for item in args:
        result += item
    return result

sum = multi_sum(1,2,3,4,5)

print("sum = %d" % sum)



#double stars ** for multiple key-values
def do_something(name, age, gender="Male", *args, **kwds):
	print("Name: %s, Age: %d, Gender: %s" % (name, age, gender))
	print(args)
	print(type(args))
	print(kwds)
	print(type(kwds))

do_something("James", 40, "Male", "Beijing", "Married", "19900001111", math=99, english=98)


a_tuple = (0, 1, 2)
print(a_tuple)
print(*a_tuple)

a_list = [0, 1, 2]
print(a_list)
print(*a_list)

a_dict = {"name":"James", "age":40, "gender":"Male"}
print(a_dict)
print(*a_dict)
print("name:{name}, age:{age}, gender:{gender}".format(**a_dict))


