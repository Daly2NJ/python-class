'''
Lecture 3 of IA241
Topic:List and Set
Date: 1/31/2023
'''

#List and type showing how to print
my_list = [1,2,3,4,5]
print(type(my_list))

#Nested list is a list within a list
my_nested_list = [1,2,3,my_list]
print(my_nested_list)

#The 0 is the first item in the list
my_list[0] = 6
print(my_list)

#Only prints the item within the list
print(my_list[4])

#To make a slice, you make an index of the first and last (not included) items 
#you want to list
print(my_list[0:1])
print(my_list[:])

#Unpack:If you know how many items are in the list, you can assign each item to
#a corresponding variable
x,y,z = ['a','b','c']
print(x)
print(y)
print(z)

#add item to a list: append(item)
my_list.append(7)
print(my_list)

#remove item from a list: remove(item)
my_list.remove(5)
print(my_list)

#sort list in rising numerical/alphabetical order: sort()
my_list.sort()
print(my_list)

#sort list in decreasing numerical/reverse alphabetical order: reverse()
my_list.reverse()
print(my_list)

#addition; list+list
print(my_list + [8,9])

#add multiple items to list: extend()
my_list.extend([8,9])
print(my_list)

#verify presence of a variable in the list
print('9' in my_list)

#determine how many items are in a list
print(len(my_nested_list))