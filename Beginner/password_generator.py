# Ask user if they want a strong or weak password. A strong password will contain lowercase letters, uppercase letters, numbers, and symbols 



import random
import string

def password():
	while True:
		answer = input("Do you want a strong password (y/n)? ")
		if (answer ==  'y'):
			n = random.randint(6, 13)
			contents = string.ascii_letters + string.digits + string.punctuation
			rletter = random.choices(contents, k = n)
			return "".join(rletter)
			break
		elif (answer == 'n'):
			elist = ['password', '1234', '0000']
			return random.choice(elist)
			break
		else:
			print("Please enter y or n")


if __name__ == '__main__':
	print(password())	
