def printStars(x):
    if x <= 0:
        print()
        return
    else:
        print('*', end = '')
        printStars(x-1)


def printTriangle(y):
    if y <= 0:
        return
    else:
        printStars(y)
        printTriangle(y-1)
        
printTriangle(5)