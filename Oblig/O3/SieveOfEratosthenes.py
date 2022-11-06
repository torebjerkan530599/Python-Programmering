def findPrimes(limit):
    primes = [True for i in range(limit+1)] #Write down all of the numbers from 0 to the limit
    p = 2
    
    #Cross out all multiples of p (but not p itself)
    while (p * p <= limit): 
        if (primes[p] == True):
            #find multiples of current p
            for i in range(p * p, limit+1, p): 
                primes[i] = False
        # Set p equal to the next number in the list that is not crossed out
        p += 1 
 
    # Report all of the numbers that have not been crossed out as prime
    for p in range(2, limit+1):
        if primes[p]:
            print(p)


def main():
    limit = int(input("Enter a limit for prime numbers between 2 and limit: "))
    findPrimes(limit)


main()