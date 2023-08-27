dec = int(input("Enter a decimal within range [0,15]: "))

# logikk: hvis vi deler et tall på 2 vil vi få en rest på 1 eller 0.1

bin4 = dec % 2 
quotient =  dec // 2

bin3 = quotient % 2
quotient =  quotient // 2

bin2 = quotient % 2
quotient =  quotient // 2

bin1 = quotient % 2
quotient =  quotient // 2

print(f'{bin1}{bin2}{bin3}{bin4}')