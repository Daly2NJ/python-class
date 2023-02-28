'''
lab7
while loop in Python
'''
#3.1
i = 6
while i > 0:
    i= i-1
    if i == 3:
        continue
    print(i)
    
#3.2
i = 1
result =1
while i<=5:
    result = result * i
    i = i + 1
print(result)

#3.3
i = 1
result = 0
while i<=5:
    result = result + i
    i = i + 1
print(result)

#3.4
i = 3
result =1
while i<=8:
    result = result * i
    i = i + 1
print(result)

#3.5
n = 1
d = 1 
numerator = 1
denominator = 1
while n<=8:
    numerator = numerator * n
    n = n + 1
while d<=3:
    denominator = denominator * d
    d = d + 1
result = numerator/denominator
print(result)

#3.6
num_list = [12, 32, 43, 35]

while num_list:
    num_list.pop()
    print(num_list)