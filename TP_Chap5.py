#5.1
import time

# Get the current time in seconds since the epoch
current_time = time.time()

# Calculate the number of days since the epoch
days_since_epoch = int(current_time // (24 * 60 * 60))

# Calculate the time of day in hours, minutes, and seconds
seconds_since_midnight = int(current_time % (24 * 60 * 60))
hours = seconds_since_midnight // 3600
minutes = (seconds_since_midnight % 3600) // 60
seconds = seconds_since_midnight % 60

# Print the results
print("Current time:", hours, "hours,", minutes, "minutes,", seconds, "seconds")
print("Days since epoch:", days_since_epoch)

#5.2
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def prompt_fermat():
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    c = int(input("Enter a value for c: "))
    n = int(input("Enter a value for n: "))
    check_fermat(a, b, c, n)

#prompt_fermat()
#The input function is used to prompt the user for the values of a, b, c, and n. The values are then converted to integers using the int function and passed to the check_fermat function.

#5.3
def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')
def prompt_and_check_triangle():
    a = int(input('Enter the length of the first stick: '))
    b = int(input('Enter the length of the second stick: '))
    c = int(input('Enter the length of the third stick: '))
    is_triangle(a, b, c)
#prompt_and_check_triangle()




