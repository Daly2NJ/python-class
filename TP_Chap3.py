#3.1
def right_justify(s):
    print(' ' * (70 - len(s)) + s)
right_justify('monty')

#3.2
# function to call a function twice
def do_twice(f):
    f()
    f()

# function to call a function twice with an argument
def do_twice_with_arg(f, arg):
    f(arg)
    f(arg)

# function to print a string twice
def print_twice(string):
    print(string)
    print(string)

# calling do_twice with print_spam function
def print_spam():
    print('spam')

do_twice(print_spam)

# calling do_twice_with_arg with print_twice function
do_twice_with_arg(print_twice, 'spam')

# function to call a function four times with an argument
def do_four(f, arg):
    do_twice_with_arg(f, arg)
    do_twice_with_arg(f, arg)
#3.3
# function to draw the horizontal lines
def draw_horizontal_line():
    print('+', '- ' * 4, '+', '- ' * 4, '+')

# function to draw the vertical lines
def draw_vertical_line():
    print('|', '  ' * 4, '|', '  ' * 4, '|')

# function to draw the grid
def draw_grid():
    draw_horizontal_line()
    for i in range(4):
        draw_vertical_line()
    draw_horizontal_line()
    for i in range(4):
        draw_vertical_line()
    draw_horizontal_line()

draw_grid()

def draw_4x4_grid():
    draw_horizontal_line() 
    for i in range(4):
        draw_vertical_line() 
    draw_horizontal_line() 
    for i in range(4):
        draw_vertical_line() 
    draw_horizontal_line() 
    for i in range(4):
        draw_vertical_line() 
    draw_horizontal_line() 
    for i in range(4):
        draw_vertical_line() 
    draw_horizontal_line() 

draw_4x4_grid()