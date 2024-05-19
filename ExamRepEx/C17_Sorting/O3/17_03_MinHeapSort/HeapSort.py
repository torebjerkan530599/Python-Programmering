from MinHeap import MinHeap

def heapSort(lst):
    heap = MinHeap() # Create a Heap 

    # Add elements to the heap
    for v in lst:
        heap.add(v)
    
    # Remove elements from the heap
    for i in range(len(lst)): 
        lst[i] = heap.remove()
  
def main():
    lst = [-44, -5, -3, 3, 3, 1, -4, 0, 1, 2, 4, 5, 53]
    lst = [1, 2.4, 2.5, 2, 1.5, 34.5, 5.5, 6, 6, 2.4, 5.5, 9]
    heapSort(lst)
    for v in lst:
        print(str(v) + " ", end = " ")

main()
