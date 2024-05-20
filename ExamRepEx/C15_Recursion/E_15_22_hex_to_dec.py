def hexToDecimal(hexString):
    hex_chars = '0123456789ABCDEF'
    if len(hexString) == 0:
        return 0
    else:
        last_char = hexString[-1].upper()
        if last_char in hex_chars:
            return hex_chars.index(last_char) + 16 * hexToDecimal(hexString[:-1])
        else:
            return -1  # Error: Invalid hex character

def main():
    hex_str = input("Enter a hex number: ")
    decimal = hexToDecimal(hex_str)
    if decimal != -1:
        print(hex_str, "is decimal", decimal)
    else:
        print("Error: Invalid hex character")

main()
