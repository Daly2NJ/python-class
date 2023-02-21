'''
Lecture 5 of IA241
Topic: If Statements
Date: 2/16/2023
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
    #x and y: If x is False, then x, else y
print(True and False)
    #x or y: If x is False, then y, else x
print(True or False)
    #not x: If x is False, then True, else False
print(not True)
#Empty data containers, empty strings, int 0, float 0.0, and None are all kinds of False
print(not None)
print(() and [])
print([] and ())
print(-1 or 0)
print(0 or -1)

#The if statement is used for conditional execution
if 2>1:
     #If the conditional test evaluates to true, Python executes the code following the if statement
    print('2>1')
    if 3>1:
        print('3>1')
    #If the test evaluates to False, Python ignores the code following the if statement 
    if 2<=1:
        print('2<=1')
print('not in the if block')

#if-else statement will take one action when a test passes a conditional test passes, and a different actionbin all other cases
#The else statement allows you to define an actionthat is executed when the conditional test fails
if 2<=1:
    print('2<=1')
else:
    print('2>1')
if 2<=2:
    print('2<=2')
else:
    print('2>2')
    
#if-elif-else chain can test more than two possible situations
#it will run each conditional test in order until one passes
#when a test passes, the code following that test is executed and Python skips the rest of the tests
if 2<=1:
    print('2<=1')
elif 2<=2:
    print('2<=2')
else:
    print('2>1')