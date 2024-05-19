def printStars(x):
    if x <= 0:
        print()
        return
    else:
        print('*', end = '')
        printStars(x-1)


def printTriangle(y):
    if y <= 0:
        print('Blast off!')
        return
    else:
        printStars(y)
        printTriangle(y-1)
        
printTriangle(5)

# alternatively, a better approach.

def countdown(n):
    # Base case: when n is 0, print "Blast off!"
    if n == 0:
        print("Blast off!")
    else:
        # Recursive case: print '*' n times, then call countdown with n-1
        print('*' * n)
        countdown(n - 1)

# Test program
def main():
    try:
        # Prompt the user to enter a number
        num = int(input("Enter a number: "))
        
        # Call the countdown function with the input number
        countdown(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()