import math

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)


def compare_values(lst, mid, high):
    return mid if lst[mid] < lst[high] else high

#median av tre: plukk ut første, siste og midterste i hver sin del-liste, sorter del-listene og bruk det midterste
def select_median_of_three(lst,first,last) -> int:
    
    middle = (first + last) // 2

    high_value = compare_values(lst, first, compare_values(lst, middle, last))

    if high_value == first:
        return compare_values(lst, middle, last)
    if high_value == last:
        return compare_values(lst, first, last)
    return high_value
        
# Partition lst[first..last] 
'''https://dev.to/smilesforgood/writing-a-median-of-three-pivot-helper-for-quicksort-289m'''
def partition(lst, first, last):
    
    low = first  # Index for forward search
    high = last  # Index for backward search
    pivot = lst[select_median_of_three(lst,low,high)]# Choose median of medians as pivot

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first

# A test function 
def main():
    #lst = [2, 7, 2, 5, 6, 1, -2, 3, 14, 12, 17,1]
    lst = [2, 22, 2, 5, -3]
    
    quickSort(lst)
    for v in lst:
        print(str(v) + " ", end = "")

main()
