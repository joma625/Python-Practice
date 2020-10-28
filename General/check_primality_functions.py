###################################################################
# ask user for a number and determine whether the number is prime or not 'using functions'
###################################################################


def check_primality(num):
    try:
        num = int(num)
    except:
        print("This is not an integer!")
        return

    for i in range(2, num // 2):
        if num % i == 0:
            print("Not a prime number!")
            return
    print("This is a prime number!")
    return


numb = input("Insert a number: ")
check_primality(numb)
