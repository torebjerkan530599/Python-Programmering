
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)

'''https://dev.to/smilesforgood/writing-a-median-of-three-pivot-helper-for-quicksort-289m'''
#median av tre: plukk ut første, siste og midterste i hver sin del-liste, sorter del-listene og bruk det midterste
def select_median_of_three(lst,first,last) -> int:
    
    middle = (first + last) // 2

    high_value = compare_values(lst, first, compare_values(lst, middle, last))

    if high_value == first:
        return compare_values(lst, middle, last)
    if high_value == last:
        return compare_values(lst, first, last)
    return high_value

def compare_values(lst, mid, high):
    return mid if lst[mid] < lst[high] else high
        
def partition(lst, first, last):
    pivotIndex = select_median_of_three(lst, first, last)
    pivot = lst[pivotIndex]
    lst[pivotIndex], lst[last] = lst[last], lst[pivotIndex]  # Move pivot to the end
    
    low = first
    high = last - 1
    
    while True:
        while low <= high and lst[low] <= pivot:
            low += 1
        while low <= high and lst[high] > pivot:
            high -= 1
        if low >= high:
            break
        lst[low], lst[high] = lst[high], lst[low]
    lst[low], lst[last] = lst[last], lst[low]  # Move pivot to its final place
    return low

# A test function 
def main():
    print("Using quicksort median of three:")
    lst1 = [2, 7, 2, 5, 6, 1, -2, 3, 14, 12, 17,1]
    quickSort(lst1)
    for v in lst1:
        print(v, end=" ")
    
    print()
    print("Actual sorted list: ")
    lst2 = [2, 7, 2, 5, 6, 1, -2, 3, 14, 12, 17,1]
    lst2.sort()
    
    for v in lst2:
        print(v, end=" ")

main()
