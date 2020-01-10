# hourglasses of a 6x6 2D Array

#(1,1), (1,2), (1,3), (2,2), (3,1), (3,2), (3,3)
#(1,2), (1,3), (1,4), (2,3), (3.2), (3,3), (3,4)
# create an empty list
# iterate i, j from 1 to 4
# sum = 0
# for i in range 4
# for j in range 4
# sum.append( i[j] + i[j+1] + i[j+2] + (i+1)[j+1] + (i+2)[j] + (i+2)[j+1] + (i+2)[j+2])

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sums = []
    for i in range(4):
        for j in range(4):
            sums.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

    print(max(sums))
