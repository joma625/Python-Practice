# generate a random number between 1 and 9, and ask the user to guess the number, then tell them if they guess too low or high. Keep the game going until user types 'exit' and print out how many guesses have taken place

import random as rd
num = rd.randint(1, 9)
count = 0

while True:
    count += 1
    guess = input("Give me a guess between 1 and 9: ")
    try:
        guess = int(guess)
    except:
        pass

    if guess == num:
        print('You got it chap! ')
        break
    elif guess == 'exit':
        print('Bye! ')
        count -= 1
        break
    elif guess < num:
        print('Too low! ')
        continue
    else:
        print('Too high!')
        continue

if count == 1:
    print('You made one guess!')
else:
    print('You made ', count, ' guesses!')
