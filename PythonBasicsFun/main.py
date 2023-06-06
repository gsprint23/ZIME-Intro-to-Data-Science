import math # to get access
# to math variables and functions

# COMMENTS
# this is a one line comment

"""
this is
a multi
line comment
"""

# GETTING INPUT FROM THE USER
print("Enter a number: ")
num = input() # num is a variable
# what type is num?
print(type(num))
print("The number doubled is:", 2 * num)

# we need to convert num from a string
# to a integer
num_int = int(num)
print("The number doubled is:", 2 * num_int)

# CONDITIONALS (IF STATEMENTS)
# if some condition is true
# then execute some code
x = 10
if x == 5:
    print("x is 5")
elif x == 7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

# LOOPS
# use a loop when you want to repeat code
# we have for loops and while loops in python
# for item in sequence:
#     body of for loop (code you want repeated)
for character in "python":
    print(character)

# we can also make our own sequences
# with range(start, stop, step)
for i in range(0, 5, 1):
    print(i)
for i in range(5):
    print(i)
for i in range(0, 5):
    print(i)

# task: write a for loop to print
# the first 20 even numbers
# 2, 4, ..., 38, 40
for i in range(2, 42, 2):
    print(i, end=" ")
print()

# while loops
# while condition is true:
#     body of loop (code to be repeated)
#     progress towards the condition
#         being false
# let's re-write our for loop
# with a while loop
i = 2
while i <= 40:
    print(i, end=" ")
    i += 2 # progress
print()

# note that conditionals and loops
# can be nested inside each other
# just pay attention to the indentation

# FUNCTIONS
# a named sequence of statements
# we have been using pre-defined
# functions
# print(), int(), input(), range(), ...
# now, we define our own functions
# def function_name(parameter list):
#    body of function (code to run
#       when function is "called")
# functions don't run until they are
# called

# example #1
# function with no inputs and no
# return
def say_hello():
    print("hello")

# we need to call the function
# for it to run
for i in range(10):
    say_hello() # call

# example #2
# function with one input and no
# return
def say(message):
    print(message)

say("hi!!")
say("how are you??")
say("goodbye...")

# example #3
# function with one input
# and one return (output)
def compute_circle_area(radius):
    area = math.pi * radius ** 2
    return area # send back to
    # calling code

result = compute_circle_area(5)
print("result:", result)
