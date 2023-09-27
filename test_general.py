
# Display table body
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10): 
        # Display the product and align properly
        print(format(i * j, '4d'), end = '')
    print()# Jump to the new line
    
    import random 
 
matrix = [] # Create an empty list 
 
numberOfRows = int(input("Enter the number of rows: ")) 
numberOfColumns = int(input("Enter the number of columns: ")) 
for row in range(numberOfRows): 
    matrix.append([])
    for column in range(numberOfColumns): 
        matrix[row].append(random.randint(0, 99))
    

print(matrix) 