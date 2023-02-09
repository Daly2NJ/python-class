'''
Chapter 8 of Think Python
Strings
2/7/2023
'''
'''
fruit ='banana'
index = 5
while index > -1:
    letter = fruit[index]
    print(letter)
    index = index-1
    
for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)
    '''
#8.2
fruit = 'banana'
print(fruit.count("a"))

#8.3
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('neon'))

#8.4
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return 'True'
        else:
            return 'False'
print(any_lowercase1('Lauge'))
#8.5
def rotate_word(string)
    for letter in string
    