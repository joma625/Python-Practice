# Write a function prompting the user for a long string containing multiple words, and then return the string back with the words in backwards order

def reverse_line ():
	string1 = input("Type a long string with many words: ").strip().split()
	string2 = string1[::-1]
	result = []

	result  = " ".join(string2)
	print(result)
		

if __name__ == '__main__':
	reverse_line()
		
