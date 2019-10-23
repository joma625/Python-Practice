# Take a number input and print out its divisors

num = int(input("Enter a number: "))

div = []
i = 1
while i <= num:
    if(num % i == 0):
        div.append(i)
    i += 1

print(div)
