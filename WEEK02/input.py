name = input("Enter your name: ")
print(name)
print(type(name))   #it will print the type of the variable 'name', which is <class 'str'> since input() returns a string.


values = input("Enter some values  ")
my_tuple=tuple(values.split())
print(my_tuple)
print(type(my_tuple))
my_tuple=set(values.split())
print(my_tuple)
print(type(my_tuple))