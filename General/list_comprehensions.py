a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# write a one-line code that makes a list of only even elements of an existing list

# ordinal
b = [j for i, j in enumerate(a) if (i + 1) % 2 == 0]

# cardinal
b = [i for i in a if i % 2 == 0]
