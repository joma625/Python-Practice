# write a function that takes a list and return a new list with only the first and the last elements of the given list


def firstlast(alist):
    try:
        newlist = [alist[0], alist[len(alist) - 1]]
        return newlist

    except Exception:
        print('This is not a list.')
        return


if __name__ == '__main__':
    a = [1, 2, 3]
    newlist = firstlast(a)
    print(newlist)
