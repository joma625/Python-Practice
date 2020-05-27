# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
# [[0, 0, 1],
# [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

#-1 if the board is not yet finished (there are empty spots),
#1 if "X" won,
#2 if "O" won,
#0 if it's a cat's game (i.e. a draw).
#You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.



################################################################################################

def is_solved(board):
    column1 = []
    column2 = []
    column3 = []

    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
        else:
            column1.append(row[0])
            column2.append(row[1])
            column3.append(row[2])

    for column in [column1, column2, column3]:
        if column[0] == column[1] == column[2]:
            return column[0]


    if column1[0] == column2[1] == column3[2]:
        return column1[0]
    if column1[2] == column2[1] == column3[0]:
        return column1[2]

    status = True 
    for i in board:
        if 0 in i:
            status = False

    if status:
        return 0
    else:
        return -1


board = [[2, 1, 2],
                 [2, 1, 1],
                          [1, 1, 2]]


print(is_solved(board))

