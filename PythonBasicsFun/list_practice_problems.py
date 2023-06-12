import random

# 1D List Practice Problem
# In ListFun, write code that generates 20 random numbers between
# 1 and 10 inclusive and puts them in a 1D list.
# The program then does the following using the list:
nums = []
for i in range(20):
    rand_num = random.randint(1, 10)
    nums.append(rand_num)
print(nums)

# Prints the numbers all one line, each number separated by a space
for num in nums:
    print(num, end=" ")
print()

# Sorts the list using a list method
nums.sort() # inplace sort
print(nums)
# nums_copy_sorted = sorted(nums) # sorts on copy and returns sorted copy
# print(nums)
# print(nums_copy_sorted)

# Prints the largest and smallest number in the list
# Hint: can you take advantage of the current ordering of your list?
print("min:", nums[0], "max:", nums[-1])
print("min:", min(nums), "max:", max(nums))

# Determines the number of times a user-specified number is in the list
user_input = int(input("Enter a number to count: "))
print("Count:", nums.count(user_input))
# OR
count = 0
for num in nums:
    if num == user_input:
        count += 1
print("Count:", count)

# Removes all instances of a user-specified number in the list. 
# If the number is not in the list print the message: 
# "Sorry, your number is not here!"
user_input = int(input("Enter a number to remove all occurences of: "))
if user_input in nums:
    while user_input in nums:
        nums.remove(user_input)
else:
    print("Sorry, your number is not here!")
print(nums)


# Note: for practice with functions, try solving this problem using functions :)

# 2D List Practice Problem
# In ListFun, write code that generates 50 random numbers between 1 and 10
# inclusive and puts them in a 2D list that is 10x5
# (e.g. 10 rows and 5 columns). The program then does the following using the list:
table = []
for i in range(10):
    # build a row
    row = []
    for j in range(5):
        # generate a random number
        rand_num = random.randrange(1, 11)
        row.append(rand_num)
    table.append(row)
print(table)

# Prints the numbers in a nice grid format (like a table)
for row in table:
    # row is a 1D list of numbers
    for num in row:
        print(num, end="\t")
    print()

# Prints the largest and smallest number in the list
# assume the first number is the smallest and the largest
curr_min = curr_max = table[0][0]
for row in table:
    for value in row:
        if value < curr_min:
            # we have a new min
            curr_min = value
        if value > curr_max:
            # we have a new max
            curr_max = value
print("min:", curr_min, "max:", curr_max)

# Determines the number of times a user-specified number is in the list
user_input = int(input("Enter a number to count: "))
count = 0
for row in table:
    for num in row:
        if num == user_input:
            count += 1
print("Count:", count)

# Removes all instances of a user-specified number in the list.
# If the number is not in the list print the message:
# "Sorry, your number is not here!"
user_input = int(input("Enter a number to remove all occurences of: "))
removed = False
for row in table:
    while user_input in row:
        row.remove(user_input)
        removed = True
if not removed:
    print("Sorry, your number is not here!")
print(table)

# Note: for practice with functions, try solving this problem using functions :)

# LIST ALIASING
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1 # not a copy!!! list3 is an "alias" for list1
print(list1, list2, list3)
list3[0] = 200
print(list1, list2, list3)

def add_one_to_each_element(some_list):
    # some_list is an alias to the same list list3 refers to
    for i in range(len(some_list)):
        some_list[i] += 1

add_one_to_each_element(list3)
print(list1, list2, list3)
# python is "pass by object reference"
# if you pass a list to a function, code in that
# function can modify the list
