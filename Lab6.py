'''
lab6
for loop, range function
'''


#3.1
for i in range(0,6):
    if i != 3:
        print(i)

#3.2
result = 1
for i in range(1,6):
    result = result * i
print(result)

#3.3
result = 0
for i in range(1,6):
    result = result + i
print(result)

#3.4
result = 1
for i in range(3,9):
    result *= i
print(result)

#3.5
numerator = 1
for i in range(1,9):
    numerator = numerator * i
denominator = 1
for i in range(1,4):
    denominator = denominator * i
result = numerator / denominator
print(result)

#3.6
result = 0 
for word in 'this is my 6th string'.split():
    result = result + 1
print(result)

#3.7
my_tweet = {
"favorite_count":1138, 
"lang": "en", 
"coordinates": (-75, 40), 
"entities": {"hashtags":["Preds", "Pens", "SingIntoSprng"]}
}
count = 0
for i in my_tweet["entities"]["hashtags"]:
    count += 1
print(count)