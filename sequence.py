#sequence types in python:
#-tuple
#-list
#-string
#-unicode string
#-buffer
#-xrange

#sting literal indexing
print("Hello")
print("Hello"[0])
print("Hello"[-1])

name = "James Han"
print(name[0])
print(name[1])
print(name[-1])
print(name[3])
print(name[7])
print(name[3:7])   #left open, right close.
print(name[3:])
print(name[:7])
print(name[:])      #from start to end, all is included.
print(name[0:-1])   #-1 is not included.
print(name[len(name)-1])
#print(name[len(name)])       #this line dose not work because of indexing error.
print(name[0:len(name)])  #name[len(name)] dose not exist actually, but using it as slice right is OK.


#nested
james = ["James Han", 40, "Male"]
frank = ["Frank Fan", 50, "Male"]
names = [james, frank]
print(names[0])
print(names[1][1])
print(names[1][2][3])



#pace - slice step
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::1])
print(numbers[::2])
print(numbers[::3])
#print(numbers[::0])   # not work - slice step can not be zero
print(numbers[::])     # slice step can be empty, then defalt to 1.
print(numbers[1:7:2])
print(numbers[1:7:-2])  #work or not? work, but empty result. pace is minus, then left should bigger than right.
print(numbers[7:1:2])   #work or not? work, but empty result. pace is positive, then left should samller than right.
print(numbers[7:1:-2])  




# + concatenate for same type sequences
print((1,2,3)+(4,5,6)+(7,8,9))
print("Hello" + " " + "Word")
#print("Hello" + [1,2,3])         #dose not work, concatenate str (not list) to str

# * multiply sequences
print("James " * 10)
print((1,2,3)*3)
print(4*[1,2,3])
print([None]*5)

#slice and assemble

abc = ["a", "b", "c"]
numbers[3:5] = abc
print(numbers)


