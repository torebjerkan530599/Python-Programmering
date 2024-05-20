def is_prime_recursive(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

# Main program
def main():
    number = int(input("Enter a whole number: "))
    if is_prime_recursive(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

main()
