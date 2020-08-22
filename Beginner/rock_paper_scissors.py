# design a two-player rock-paper-scissors game

# while True:
#     answer1 = input("Rock, Paper, or Scissors? ")
#     answer2 = input("Rock, Paper, or Scissors? ")

#     if(answer1 == answer2):
#         print("Draw, next game! ")
#         continue
#     elif((answer1 == 'Rock' and answer2 == 'Paper') or (answer1 == 'Paper' and answer2 == 'Scissors') or (answer1 == 'Scissors' and answer2 == 'Rock')):
#         print('Player2 wins! Next game!')
#         continue
#     else:
#         print('Player1 wins! Next game!')
#         continue


# solution using dictionary

roshambo = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

while True:
    user1 = input('User1 please take your pick: ')
    user2 = input('User2 please take your pick: ')
    diff = roshambo[user1] - roshambo[user2]

    if diff in [-1, 2]:
        print('User2 is the winner! Next Game!')
    elif diff == 0:
        print('Tie! Next Game!')
    else:
        print('User1 wins! Next Game!')
