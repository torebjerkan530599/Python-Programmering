import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(8, -1, -1):
        count[i] += count[i + 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    random_integers = [random.randint(100, 999) for _ in range(100)]
    print("Original list of random three-digit integers:")
    print(random_integers)
    
    radix_sort(random_integers)
    print("\nSorted list in reverse order:")
    print(random_integers)
