from pathlib import Path


def main():
    n = 10000#0000#00 # 10 billion takes too long for my old computer!

    # A list to hold prime numbers
    list = [] 

    NUMBER_PER_LINE = 10  # Display 10 per line
    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness
    squareRoot = 1  # Check whether number <= squareRoot
    filepath = Path(__file__).parent / "Exercise16_08.dat"
    outputFile = open(filepath, "w")

    # Repeatedly find prime numbers
    while number <= n:
        # Assume the number is prime
        isPrime = True  # Is the current number prime?

        if squareRoot * squareRoot < number:
            squareRoot += 1

        # Test whether number is prime
        k = 0
        while k < len(list) and list[k] <= squareRoot:
            if number % list[k] == 0: # If true, not prime
                isPrime = False  # Set isPrime to false          
                break  # Exit the for loop
            k += 1

        # Print the prime number and increase the count
        if isPrime:
            count += 1  # Increase the count
            list.append(number)  # Add a new prime to the list
            if count % NUMBER_PER_LINE == 0:
                # Print the number and advance to the new line
                outputFile.write(str(number) + "\n");
            else:
                outputFile.write(str(number) + " ")

        # Check whether the next number is prime
        number += 1

    print("The total number of prime number <=", n, "is", count)
    outputFile.close()
    
main()
