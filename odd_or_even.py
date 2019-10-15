# prompt user for a number
num = int(input("Enter a numnber: "))

# let the user know if the number is a multiple of 4
if(num % 4 == 0):
    print("The number is the multiple of 4.")
    quit()

# if it is not 4, let the user know the number is odd or even
if(num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

# prompt user to input two numbers
check, divide = [int(i) for i in input("Enter two numbers: ").split()]

# let the user know if the first number can be divided by the second number
if(check % divide == 0):
    print("Evenly divided!")
else:
    print("Not evenly divided!")
