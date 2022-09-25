for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
        print(j if j <= i else " ", end = " ")
    print()