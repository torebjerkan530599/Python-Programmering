def sumDigits(n):
    # Base case: If n is a single digit, return n
    if n < 10:
        return n
    else:
        # Recursive case: Extract the last digit, add it to the sum of the digits of the rest of the number
        return n % 10 + sumDigits(n // 10)

# Test program
def main():
    try:
        # Prompt the user to enter an integer
        num = int(input("Enter an integer: "))
        
        # Compute the sum of its digits
        digit_sum = sumDigits(abs(num))

        # Display the sum of the digits
        print("Sum of the digits:", digit_sum)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
