def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

def main():
    try:
        # Prompt the user to enter a number and the power
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent (a positive integer): "))
        
        # Calculate the result using the power function
        result = power(base, exponent)
        
        # Display the result
        print(f"{base} raised to the power of {exponent} is equal to {result}")
    except ValueError:
        print("Please enter valid input.")

if __name__ == "__main__":
    main()
