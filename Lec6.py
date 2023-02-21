'''
Lec 6
for loop
range function
'''
'''
For loops iterate over the items of any sequence, 
in the order they appear in the sequence
for item in sequence:
    do somthing with current item
'''
for num in [1,2,3]:
    if num>1:
        print(num)
    
for word in 'this is lec6'.split():
    print(word)
    for c in word:
        print(c)

#range() function generates arithmatic progressions
#range(m) generates progression from 0 to m-1
for i in range(5):
    print(i)
#range(n,m) generates progression from n to m-1
for i in range(1,5):
    print(i)
'''
range(n,m,step) generates progression from n to m-1 with an
increment of the step
'''
for i in range(1,5,2):
    print(i)
'''
Designing algorithms is interesting, intellectually 
challenging, and a central part of computer science

Problem: use for loop to find out the maximal item in 
the num_list = [213, 321, 123, 312]
'''
num_list = [213, 321, 123, 312]
max_item = num_list[0]
for num in num_list:
    if max_item <= num:
        max_item = num
print(max_item)