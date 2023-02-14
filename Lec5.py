'''
Lecture 3 of IA241
Topic: Dictionaries and Tuples
Date: 2/9/2023
'''

#import this

#print (1+15+
#           4564)

#all values and data containers are objects
a = 1
b = 1
#id() function returns the identity of an object
print(id(a))
print(id(b))
print(id(1))
#== operator compares the value of two objects
print(a == b)
#is operator compars the identity of two objects
print(a is b)

#None is a datatype of its own that indicates no value
a = None

print(id(a))
print(id(None))

print (a is None)
print (a == None)
#only None can be None
x = []
print(x is None)

#Boolean data is True|False
#and, or, and not operators
    #
print(True and False)