SIZE = 8  # The size of the chessboard
solutions = []  # Store all solutions

# Check if a queen can be placed at row i and column j
def isValid(row, column, queens):
    for i in range(1, row + 1):
        if (queens[row - i] == column  # Check column
                or queens[row - i] == column - i  # Check upleft diagonal
                or queens[row - i] == column + i):  # Upright diagonal
            return False  # There is a conflict
    return True  # No conflict

def findPosition(k, queens):
    start = queens[k] + 1  # Search for a new placement

    for j in range(start, SIZE):
        if isValid(k, j, queens):
            return j  # (k, j) is the place to put the queen now

    return -1

# Search for all solutions starting from a specified row
def search():
    queens = [-1] * SIZE  # Queen positions
    k = 0
    while k >= 0:
        # Find a position to place a queen in the kth row
        j = findPosition(k, queens)
        if j < 0:
            queens[k] = -1
            k -= 1  # Backtrack to the previous row
        else:
            queens[k] = j
            if k == SIZE - 1:  # If the last row is reached
                solutions.append(queens.copy())  # Store the solution
                queens[k] = -1  # Backtrack to find new solutions
                k -= 1
            else:
                k += 1

    return solutions

# Call the search function to find all solutions
solutions = search()

# Print all solutions to the console
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in range(SIZE):
        line = ['.'] * SIZE
        line[solution[row]] = 'Q'
        print(' '.join(line))
    print()

print(f"Total number of solutions: {len(solutions)}")
