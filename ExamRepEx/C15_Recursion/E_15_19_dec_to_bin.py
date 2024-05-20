def decimalToBinary(value):
    if value == 0:
        return '0'
    elif value == 1:
        return '1'
    else:
        return decimalToBinary(value // 2) + str(value % 2)

def main():
    decimal = int(input("Enter a decimal integer: "))
    binary = decimalToBinary(decimal)
    print(decimal, "is binary", binary)

main()
