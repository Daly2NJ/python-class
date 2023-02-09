'''
Lecture 3 of IA241
Topic: Dictionaries and Tuples
Date: 2/9/2023
'''

my_tuple = 'a','b','c','d','e'

print(type(my_tuple))
#A tuple is a sequence of values that is like a list, but it is immutable

not_a_tuple = ('a')
print(type(not_a_tuple))
#One value in () is not a tuple

print(my_tuple[0:2])
#most list operators also work on tuples
'''
my_tuple[0] = 'f'
print(my_tuple)
''' # Tuple values cannot be changed

my_car = {'color':'white','maker':'Buick','year':2001, 'status':'KIA'}
# A dictionary is a collection of key-value pairs
# created within {} or dict() function
# keys can be string or number

print(my_car['color'])
print(my_car['year'])
print(my_car)
#values can be string, number, list, variable, or dictionary
# to access values, call the corresponding keys

print(my_car.items())
#items() returns a list of key-value tuples
print(my_car.keys())
#keys() method returns a list of keys
print(my_car.values())
#values() method returns a list of values
print(my_car.get('year'))
#get() method returns the value of an existing key
my_car['model'] = 'Century'
#Add a new key-value pair: dict[new_key] = new_value
my_car['year'] = 2002
#Update the value of an existing key: dict[existing_key] = new_value
print(my_car)
print(len(my_car))
#len() fuction returns the number of key-value pairs
print('color' in my_car)
# in operator checks whether a ky is in th dictionary