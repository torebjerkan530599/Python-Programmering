
def isConsecutiveFour(values):
    count = 0
    for i in range(len(values)):
        if(values[i] == values[i-1] and i > 0):
            count += 1
            if(count == 3): #3 comparasions to detect 4 consecutive values
                return True
    return False


def main():
    # Read numbers as a string from the console 
    s = input("Enter numbers separated by spaces on one line: ") 
    items = s.split() # Extract items from the string 
    values = [int(x) for x in items] # Convert items to numbers
    print("4 consecutive numbers: " + str(isConsecutiveFour(values)))


main()