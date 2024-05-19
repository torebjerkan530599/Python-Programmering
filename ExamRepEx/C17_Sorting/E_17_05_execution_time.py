import random
import time
import heapq
import copy

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort
def heap_sort(arr):
    heapq.heapify(arr)
    arr[:] = [heapq.heappop(arr) for _ in range(len(arr))]

# Counting Sort helper for Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

# Radix Sort
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Helper function to measure sorting time
def measure_time(sort_fn, data):
    start_time = time.time()
    sort_fn(data)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

# Main function to generate data, sort it, and print the results
def main():
    sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    sort_algorithms = {
        'Selection': selection_sort,
        'Bubble': bubble_sort,
        'Merge': merge_sort,
        'Quick': quick_sort,
        'Heap': heap_sort,
        'Radix': radix_sort
    }

    # Print table header
    print(f"{'Array Size':<10}", end="")
    for name in sort_algorithms.keys():
        print(f"{name:<12}", end="")
    print()

    # Measure and print execution times
    for size in sizes:
        data = [random.randint(100, 999) for _ in range(size)]
        print(f"{size:<10}", end="")

        for name, sort_fn in sort_algorithms.items():
            data_copy = copy.deepcopy(data)
            time_taken = measure_time(sort_fn, data_copy)
            print(f"{time_taken:<12.0f}", end="")
        
        print()

if __name__ == "__main__":
    main()
