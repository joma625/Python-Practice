# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 2. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 3. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


# take input of name and age
name, age = input("Please enter your name and age: ").split()

# calculate the year they turn 100
year100 = (100 - int(age)) + 2019

# create message addressing them by their name and telling them when they turn 100
message = name + ', you turn 100 at year ' + str(year100) + '!'

# take input of a number and print the message that number of time
number = input("Enter a number: ")
num = int(number)
for i in range(num):
    print(message)
