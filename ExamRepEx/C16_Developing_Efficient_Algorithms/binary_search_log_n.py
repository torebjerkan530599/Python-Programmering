arr = [1,2,3,4,5,6,7,8]


def binary_search(arr,start,end,target):
    if start > end:
        return False
    mid_index = (start + end) // 2
    
    if arr[mid_index] is target:
        return mid_index
    
    if arr[mid_index] > target:    
        return binary_search(arr,0,mid_index -1, target)
    else:
        return binary_search(arr,mid_index + 1, end, target )

target = 9
print(binary_search(arr,0,len(arr)-1,target))