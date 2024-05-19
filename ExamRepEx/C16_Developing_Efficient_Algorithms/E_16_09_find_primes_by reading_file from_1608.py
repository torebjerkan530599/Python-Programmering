from pathlib import Path

def read_primes_from_file(filepath):
    primes = []
    with open(filepath, 'r') as file:
        for line in file:
            for number in line.split():
                primes.append(int(number))
    return primes

def count_primes_up_to_limit(primes, limit):
    count = 0
    for prime in primes:
        if prime <= limit:
            count += 1
        else:
            break
    return count

def main():
    # File path for the generated prime numbers
    filepath = Path(__file__).parent / "Exercise16_08.dat"

    # Limits to check
    limits = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

    # Read primes from the file
    primes = read_primes_from_file(filepath)

    # Print the number of primes less than or equal to each limit
    for limit in limits:
        prime_count = count_primes_up_to_limit(primes, limit)
        print(f"The number of prime numbers less than or equal to {limit} is {prime_count}")

main()
