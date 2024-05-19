# O(n)

def find_smallest_divide_and_conquer(arr):
    # Base case: if the list contains only one element, return that element
    if len(arr) == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively find the smallest element in each half
    smallest_left = find_smallest_divide_and_conquer(left_half)
    smallest_right = find_smallest_divide_and_conquer(right_half)
    
    # Return the smaller of the two
    return min(smallest_left, smallest_right)

# Example usage
numbers = [34, 17, 23, 2, 41, 3, 9]
smallest_number = find_smallest_divide_and_conquer(numbers)
print(f"The smallest number in the list is: {smallest_number}")

