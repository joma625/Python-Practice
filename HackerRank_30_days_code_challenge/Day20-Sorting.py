# Bubble sort

# take inputs
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# sort
nswap = 0
for j in range(n - 1):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            nswap = nswap + 1

print("Array is sorted in %s swaps." % nswap)
print("First Element: %s" % a[0])
print("Last Element: %s" % a[len(a) - 1])
