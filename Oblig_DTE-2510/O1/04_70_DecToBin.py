dec = int(input("Enter a decimal number between 0 and 15: "))

bin4 = dec % 2 
quotient =  dec // 2

bin3 = quotient % 2
quotient =  quotient // 2

bin2 = quotient % 2
quotient =  quotient // 2

bin1 = quotient % 2
quotient =  quotient // 2

print(f'{bin1}{bin2}{bin3}{bin4}')