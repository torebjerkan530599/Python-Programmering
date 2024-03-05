#median av tre: plukk ut første, siste og midterste i hver sin del-liste, sorter del-listene og bruk det midterste


def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)

# Partition lst[first..last] 
def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

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
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12, 17,1]
    
    #median av tre: plukk ut første, siste og midterste i hver sin del-liste, sorter del-listene og bruk det midterste
    
    lst_of_lst = []
    last_index = 0
    for i in range(len(lst)-4):
        if i % 5 == 0:
            lst_of_lst.append(lst[i:i+5])
            last_index = i+5
    
    
    temp = lst[last_index: len(lst)]
    lst_of_lst.append(temp)
    
    print(lst_of_lst)
    
    # lst_a = lst[0:5]
    # lst_a.sort()
    # print(lst_a)
    
    # lst_b = lst[5:10]
    # lst_b.sort()
    # print(lst_b)
    
    # med_a = lst_a[2:3]
    # med_b = lst_b[2:3]
    
    # print(med_a)
    # print(med_b) 
    
    
    quickSort(lst)
    for v in lst:
        print(str(v) + " ", end = "")

main()

# // L is the array on which median of medians needs to be found.
# // k is the expected median position. E.g. first select call might look like:
# // select (array, N/2), where 'array' is an array of numbers of length N

# select(L,k)
# {

#     if (L has 5 or fewer elements) {
#         sort L
#         return the element in the kth position
#     }

#     partition L into subsets S[i] of five elements each
#         (there will be n/5 subsets total).

#     for (i = 1 to n/5) do
#         x[i] = select(S[i],3)

#     M = select({x[i]}, n/10)

#     // The code to follow ensures that even if M turns out to be the
#     // smallest/largest value in the array, we'll get the kth smallest
#     // element in the array

#     // Partition array into three groups based on their value as
#     // compared to median M

#     partition L into L1<M, L2=M, L3>M

#     // Compare the expected median position k with length of first array L1
#     // Run recursive select over the array L1 if k is less than length
#     // of array L1
#     if (k <= length(L1))
#         return select(L1,k)

#     // Check if k falls in L3 array. Recurse accordingly
#     else if (k > length(L1)+length(L2))
#         return select(L3,k-length(L1)-length(L2))

#     // Simply return M since k falls in L2
#     else return M
