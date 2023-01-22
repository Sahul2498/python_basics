# immutable we cant change value
# surrounded by () bracket
# when we use single item or value in tuple it will take as int or str
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
# values (items) between bracket
a=(2,2.5,True,'Sahul',2,22,2,56,2.5,2)
print(a.count(2))
print(a.index(22))
print(type(a))
# we can convert tuple to list 
b=list(a)
del a

#unpacking tuples

coordinates = (1,2,3)
'''
instead of writing like this we use 
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]'''
x,y,z = coordinates #unpacking
print(x)