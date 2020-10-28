# 1. take two lists 2. randomly generate two lists
# And write one line of code to print out the list of overlapping numbers

# 1.
import sys
print('Please input two lists')
raw_lists = sys.stdin.readlines()

adj_lists = []
for line in raw_lists:
    adj_lists.append(line.rstrip())

list1, list2 = adj_lists
list1 = list1.split()
list2 = list2.split()

# 2.
# import random as rd

# el1 = rd.randint(1, 20)
# el2 = rd.randint(1, 20)
# list1 = rd.sample(range(100), el1)
# list2 = rd.sample(range(100), el2)

# one line that prints out list of overlapping numbers
print([item for item in list1 if item in list2])
