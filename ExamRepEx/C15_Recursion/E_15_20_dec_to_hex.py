def decimalToHex(value):
    if value < 16:
        return hexDigits(value)
    else:
        return decimalToHex(value // 16) + hexDigits(value % 16)

def hexDigits(digit):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def main():
    decimal = int(input("Enter a decimal integer: "))
    hex_str = decimalToHex(decimal)
    print(decimal, "is hex", hex_str)

main()
