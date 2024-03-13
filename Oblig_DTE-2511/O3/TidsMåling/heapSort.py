from Heap import Heap

def heapSort(lst):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lst:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lst)): 
        lst[len(lst) - 1 - i] = heap.remove()