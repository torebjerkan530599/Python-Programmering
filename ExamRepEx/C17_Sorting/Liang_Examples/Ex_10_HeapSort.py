from ExamRepEx.C17_Sorting.Liang_Examples.Ex_09_Heap import Heap

def heapSort(lst):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lst:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lst)): 
        lst[len(lst) - 1 - i] = heap.remove()
  
def main():
    lst = [-44, -5, -3, 3, 3, 1, -4, 0, 1, 2, 4, 5, 53]
    lst = [3,5,1,19,11]
    heapSort(lst)
    for v in lst:
        print(str(v) + " ", end = " ")

main()
