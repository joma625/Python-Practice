# write a function that asks user for how many Fibonacci numbers to generate and generate them


def fibo(num):
    fibos = []
    for i in range(num):
        if i < 2:
            fibos.append(1)
        else:
            fibos.append(fibos[i - 2] + fibos[i - 1])
    return fibos


if __name__ == '__main__':
    num = int(input("How many Fibonacci numbers do you want? "))
    print(fibo(num))
