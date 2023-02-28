'''
Lecture 7
While loop
2/28/2023
'''
#while loop
#for repeated execution as long as a condition is true
'''
while condition is True:
    do something here
'''
i = 5
while i >=0:
    i=i-1
    print(i)
#The condition needs to be changed each time, 
#otherwise the while loop will be a dead loop
i = 5
while i >0:
    print(i)
    i=i-1
#break statement: breaks out of the smallest enclosing for or while loop
i = 5
while i >= 0:
    i=i-1
    if i == 3:
        break
    print(i)
#continue statement: skips the current iteration and 
#continues with the next iteration of the loop
i = 5
while i >= 0:
    i=i-1
    if i == 3:
        continue
    print (i)
'''
pass statement: does nothing
It can be used when a statement is required syntactically 
but the program requires no action
'''
i = 5
while i >= 0:
    i=i-1
    if i == 3:
        pass
    print (i)
#Errors detected during executionare called exeptions.
#try clause: executes code
try:
    print(1/0)
#except clause: handles errors if happened in the try block
except ZeroDivisionError:
    print('division by zero')
'''
If no exception occurs, the except clause is skipped
If an exception occurs, the rest of the try clause is skipped. 
The except clause is executed
'''