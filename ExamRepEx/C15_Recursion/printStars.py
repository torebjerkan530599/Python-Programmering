def printStars(x):
    if x <= 0:
        return
    else:
        print('*', end = '')
        printStars(x-1)

printStars(10)