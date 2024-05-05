import random

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = random.choice(lst)
    less_than_pivot = list(filter(lambda x: x < pivot,lst)) #less_than_pivot = [x for x in lst if x < pivot]
    equal_to_pivot = list(filter(lambda x: x == pivot,lst)) #equal_to_pivot = [x for x in lst if x == pivot]
    greater_than_pivot = list(filter(lambda x: x > pivot,lst))# greater_than_pivot = [x for x in lst if x > pivot]
    
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)
    
    
lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
lst = quicksort(lst)
print(lst)
    
    
    