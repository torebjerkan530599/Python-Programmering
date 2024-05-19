def find_longest_same_number_sequence(nums):
    if not nums:
        return "No numbers were entered."
    
    longest_start_index = 0
    longest_length = 0
    
    current_start_index = 0
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                longest_start_index = current_start_index
            current_start_index = i
            current_length = 1
    
    # Check the last sequence
    if current_length > longest_length:
        longest_length = current_length
        longest_start_index = current_start_index
    
    return longest_start_index, longest_length, nums[longest_start_index]

# Sample run
input_sequence = input("Enter numbers separated by spaces from one line ending with 0: ").strip().split()
numbers = [int(num) for num in input_sequence if num.isdigit()]

# Removing the trailing 0
if numbers and numbers[-1] == 0:
    numbers.pop()

start_index, length, number = find_longest_same_number_sequence(numbers)
print(f"The longest same number sequence starts at index {start_index} with {length} values of {number}")
