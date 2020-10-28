#!/usr/bin/env python3

#######################PROMPT####################################
#Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
#A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
#Example scoring
#
# Throw       Score
# ---------   ------------------
# 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
# 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
# 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
#In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.

###########################################################################################

# pseudo
# def score(dice):
#   number = 0 
#   count = 0
#   dict = {number: count}
#   for item in dice:
#       number = item
#       dict.add({number: count=count+1})
#   point = 0 
#   for k, v  in dict:
#       if k == 1:
#           if count == 1:
#               point = point + 100
#           elif count == 3:
#               point = point + 1000
#       if k == 2:
#           if count == 3:
#               point = point + 200
#       if k == 3:
#           if count == 3:
#               point = point + 300
#       if k == 4:
#           if count == 3:
#               point = point + 400
#       if k == 5:
#           if count == 1:
#               point = point + 50
#           elif count == 3:
#               point = point + 500
#       if k == 6:
#           if count == 3:
#               point = point + 600
#
#   return point

# solution
def score(dice):

    score_dict = {}

    for roll in dice:
        if roll not in score_dict.keys():
            score_dict[roll] = dice.count(roll)
        else:
            continue

    # add up the points
    points = 0
    for num, count in score_dict.items():
        if num == 1:
            if count < 3:
                points = points + 100 * count
            elif count >= 3:
                points = points + 1000 + 100 * (count-3)
        elif num == 2:
            if count >= 3:
                points = points + 200
        elif num == 3:
            if count >= 3:
                points = points + 300
        elif num == 4:
            if count >= 3:
                points = points + 400
        elif num == 5:
            if count < 3:
                points = points + 50 * count
            elif count >= 3:
                points = points + 500 + 50 * (count-3)
        elif num == 6:
            if count >= 3:
                points = points + 600

    return points


#testing
print(score([2,4,4,5,4]))








