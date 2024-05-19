def linear_search(lst, target):
    steps = 0
    for index, value in enumerate(lst):
        steps += 1
        if value == target:
            return index, steps
    return -1, steps

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps

def main():
    # Create a list of numbers from 1 to 100
    numbers = list(range(1, 101))

    # Prompt the user to enter a number to find
    target = int(input("Enter a number to find (1-100): "))

    # Perform linear search
    lin_index, lin_steps = linear_search(numbers, target)
    print(f"Linear search found the number at index {lin_index} in {lin_steps} steps.")

    # Perform binary search
    bin_index, bin_steps = binary_search(numbers, target)
    print(f"Binary search found the number at index {bin_index} in {bin_steps} steps.")

if __name__ == "__main__":
    main()
