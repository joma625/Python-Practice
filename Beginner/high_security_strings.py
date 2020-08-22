#!/usr/bin/env/ python3 

# estimate the strength of a password by adding up the respective weight of each letter in the password.
# input: first line is the password; second line is an integer denoting the weight of a
# constraints: 1<= |password| <= 100
# 0 <= weight_a <= 25

import math
import os
import random
import re
import sys
import string


def getStrength(password, weight_a):
	# assign values to all lowercase letters
	avalue = {}
	for weight, i in enumerate(string.ascii_lowercase, weight_a):
		if weight <= 25:
			avalue.update({i:weight})	
	n = len(avalue)
	if n != 26:
		for weight, i in enumerate(string.ascii_lowercase[len(avalue):], 0):
			avalue.update({i:weight})

	# add up the values by letters in the password
	sumv = 0
	for i in password:
		sumv = sumv + avalue[i]
	return sumv



if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	password = input()

	weight_a = int(input().strip())

	strength = getStrength(password, weight_a)

	fptr.write(str(strength) + '\n')

	fptr.close()






