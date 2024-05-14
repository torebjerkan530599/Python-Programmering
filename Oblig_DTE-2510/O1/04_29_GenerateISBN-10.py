isbn = input("Enter the first 9 digits of an ISBN as a string: ")

if(len(isbn) != 9):
    print("Incorrect input. It must have exact 9 digits")
    exit
else:
    d1 = int(isbn[0])
    d2 = int(isbn[1])
    d3 = int(isbn[2])
    d4 = int(isbn[3])
    d5 = int(isbn[4])
    d6 = int(isbn[5])
    d7 = int(isbn[6])
    d8 = int(isbn[7])
    d9 = int(isbn[8])
    checksum = (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
    if(checksum == 10):
        print(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9) +"X")
    else:
        print(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(checksum))
    
