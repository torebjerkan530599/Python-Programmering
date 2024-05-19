import math

def is_prime_iterative(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisors from 5 to the square root of n
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Main program
def main():
    number = int(input("Enter a whole number: "))
    if is_prime_iterative(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

main()

# time complexity sqrt(n) because it only checks divisors up to sqrt(n)