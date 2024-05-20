moves = 0  # Global variable to store the number of moves

def main():
    global moves  # Access the global variable
    n = int(input("Enter number of disks: "))

    # Find the solution recursively
    moveDisks(n, 'A', 'B', 'C')
    print("Number of moves is:", moves)

# The function for finding the solution to move n disks
# from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global moves  # Access the global variable
    if n == 1:  # Stopping condition
        moves += 1
        print("Move disk", n, "from", fromTower, "to", toTower)
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        moves += 1
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)

main()  # Call the main function
