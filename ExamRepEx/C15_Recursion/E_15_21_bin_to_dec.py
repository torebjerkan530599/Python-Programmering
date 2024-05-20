def binaryToDecimal(binaryString):
    if len(binaryString) == 0:
        return 0
    else:
        last_digit = int(binaryString[-1])
        return last_digit + 2 * binaryToDecimal(binaryString[:-1])
    

# iteartive version
# def binaryToDecimal(binary):
#     decimal = 0
#     power = 0
#     for digit in reversed(binary):
#         if digit == '1':
#             decimal += 2 ** power
#         power += 1
#     return decimal

def main():
    binary = input("Enter a binary number: ")
    decimal = binaryToDecimal(binary)
    print(binary, "is decimal", decimal)

main()
