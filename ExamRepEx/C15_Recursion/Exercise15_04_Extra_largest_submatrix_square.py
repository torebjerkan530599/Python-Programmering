def main():
    size = int(input("Enter the number of rows in the square matrix: "))

    m = []
    print("Enter the matrix row by row: ", end = ' ')

    for i in range(size):
        s = input()
        m.append([int(x) for x in s.split()])

    maxSize = 0
    for i in range(size):
        for j in range(size):
            temp = getSize(i, j, m)
            if maxSize < temp: 
                maxSize = temp
    
    print("The size of a maximum square submatrix is", maxSize)

def getSize(i, j, m):
    n = len(m)
    if i == n - 1 or j == n - 1:
        return m[i][j]
    
    if m[i][j] == 1:
        return 1 + min(getSize(i, j + 1, m), 
            min(getSize(i + 1, j + 1, m), getSize(i + 1, j, m)))
    else:
        return 0
    
main()