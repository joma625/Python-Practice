# Write a program that removes the duplicates off of a list
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

# loop
# def dedup(list):
#     for item in list:
#         if list.count(item) > 1:
#             list.remove(item)

#     return list

# sets


alist = [1, 2, 3, 3, 4, 5]
# print(dedup(alist))
newlist = set(alist)
print(newlist)
