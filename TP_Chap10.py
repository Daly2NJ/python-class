'''
Chapter 10 of Think Python
Lists
2/9/2023
'''
#10.1
def nested_sum(t):
    total = 0
    for s in t:
        for i in s:
            total += i
    return total
numbers = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(numbers))

#10.2
def cumsum(t):
    result = []
    total = 0
    for i in t:
        total += i
        result.append(total)
    return result
numbers = [1, 2, 3]
print(cumsum(numbers))

#10.3
def middle(t):
    return t[1:-1]
numbers = [1, 2, 3, 4]
print(middle(numbers))

#10.4
def chop(t):
    if len(t) > 2:
        t.pop(0)
        t.pop(-1)
numbers = [1, 2, 3, 4]
chop(numbers)
print(numbers)

#10.5
def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))

#10.6
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
print(is_anagram('salts', 'lasts'))

#10.7
def has_duplicates(t):
    return len(t) != len(set(t))
numbers = (1, 2, 3, 4, 2, 5)
print(has_duplicates(numbers))

#10.8
import random
def same_birthday(n_students):
    birthdays = [random.randint(1, 365) for i in range(n_students)]
    return len(set(birthdays)) != n_students
def estimative_probability(n_students, n_simulations):
    count = 0
    for i in range(n_simulations):
        if same_birthday(n_students):
            count += 1
    return count/n_simulations
print(estimative_probability(23, 10000))

#10.10
def in_bisect(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) / 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
