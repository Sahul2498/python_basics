# list in python
"""
list are comma seperated values and uses [] brackets to store it 
list is mutable, which means we can change the values
use [] brackets
List is a collection which is ordered and changeable. Allows duplicate members.
list is a form of array 
"""
a=[1,2,6,4,5]
# print(a)
# print(type(a))
a[0]=100
print(a)
# #slicing
# print(a[1])
# #it will print from reverse
# print(a[-1])
# #it will print from starting 0th index to 2nd index
# print(a[0:3])
# #it will start print from 2nd index to the ending index
# print(a[2:])
# #it will start print from 0th index to previous of 3rd index
# print(a[:3])

# print("---------------------------")
a=[1,True,'Ram',2.5]
print(a)
print(type(a))
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(type(a[3]))

# print('----------------------------')

# a=[10,25,35,45,25,4,25]
# print(a)
# # .clear is used to remove all the elements in the list 

# a.clear()

# print(a)

# # .copy returns a copy of the specified list
# # copy the [a] list

# a=[10,25,35,45]
# b=a.copy()
# print(b)

# # .count return the no of times the value appears in the list

# a=[10,25,35,45,25,4,25]
# print(a.count(25))

# # .index will returns the position at the first occurrence of the specified value

# a=[10,25,35,45,25,4,25]
# print(a.index(25))

# '''# len will show the length of the list

# print(len(a))

# # max will give the highest value in the list 
# print(max(a))
# # min will give the lowest value in the list   
# print(min(a))

# # .pop will remove element using index

# a=[10,25,35,45,25,4,25]
# a.pop(2)
# print(a)
# #The pop() method returns removed value

# fruits = ['apple', 'banana', 'cherry']
# x = fruits.pop(1)
# print(x)

# # .remove will remove the first occurence it will remove value

# a=[10,25,35,45,25,4,25]
# a.remove(25)
# print(a)

# # .append will add an element at the end of the list

# names=['Ram']
# print(names)
# names.append('Sahul')
# names.append('kumar')
# print(names)'''

# # .extend it adds specified list elements to the end of the current list
# # ex:add the elements of cars to fruits list

# '''fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# # addinng a tuple to the list
# fruits = ['apple', 'banana', 'cherry']
# points = (1, 4, 5, 9)
# fruits.extend(points)'''

# # .insert  will insert values based on index at specified position
# '''
# names=['Sahul','Hari','Garwin','Kumar']

# names.insert(2,'Najeeb')
# '''
# #list constructor(list())use panna adha list constructor, nama endha valueah list ah convert pannikum 
# print(list(range(5)))
# print(list('sahul'))
# print('---------------------------')

# # sort is used to asscending and desscending values in the list ,it can be both strings and int but the input should be in same data type

# a=[12,10,54,200,85,150]
# a.sort()
# print(a)

# # .reverse method reverses the sorting order of the elements.
# a=[1,10,54,85,200,150]
# a.reverse()
# print(a)

# #sort is used to asscending and desscending values in the list ,it can be both strings and int but the input should be in same data type
# a=[12,10,54,200,85,150]
# x=sorted(a)
# print(x)

# a=[12,10,54,200,85,150]
# x=sorted(a,reverse=True)
# print(x)