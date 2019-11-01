# ask user for a string and tell him whether it is a palindrome or not

word = input("Enter a string: ")

n = len(word)
if(word[:] == word[n::-1]):
    print("This is a palindrome!")
    quit()
print("This is not a palindrome!")
