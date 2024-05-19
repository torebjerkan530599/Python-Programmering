class MinHeap:
    def __init__(self):
        self.__lst = []

    # Add a new item into the lst 
    def add(self, e):
        self.__lst.append(e)  # Append to the lst
        # The index of the last node
        currentIndex = len(self.__lst) - 1
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and self.__lst[currentIndex] < self.__lst[parentIndex]:
            self.__lst[currentIndex], self.__lst[parentIndex] = self.__lst[parentIndex], self.__lst[currentIndex]
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    # Remove the root from the lst 
    def remove(self):
        if len(self.__lst) == 0:
            return None
    
        removedItem = self.__lst[0]
        self.__lst[0] = self.__lst[len(self.__lst) - 1]
        self.__lst.pop(len(self.__lst) - 1) # Remove the last item
    
        currentIndex = 0
        while currentIndex < len(self.__lst):
            leftChildIndex = 2 * currentIndex + 1
            rightChildIndex = 2 * currentIndex + 2
          
            # Find the minimum between two children
            if leftChildIndex >= len(self.__lst): 
                break  # The tree is a lst
            maxIndex = leftChildIndex
            if rightChildIndex < len(self.__lst):
                if self.__lst[maxIndex] > self.__lst[rightChildIndex]:
                    maxIndex = rightChildIndex
          
            # Swap if the current node is less than the minimum 
            if self.__lst[currentIndex] > self.__lst[maxIndex]:
                self.__lst[maxIndex], self.__lst[currentIndex] = \
                    self.__lst[currentIndex], self.__lst[maxIndex]
                currentIndex = maxIndex
            else:
                break  # The tree is a lst
    
        return removedItem
  
    # Returns the size of the heap
    def getSize(self):
        return len(self.__lst)

    # Returns True if the heap is empty
    def isEmpty(self):
        return self.getSize() == 0

    # Returns the largest element in the heap without removing it
    def peek(self):
        return self.__lst[0]
        
    # Returns the list in the heap
    def getLst(self):
        return self.__lst   
    
    def validate(self):
        n = len(self.__lst)
        for i in range(2):
            if self.__lst[i // 2] > self.__lst[i]: 
                return False
        return True

    def __str__(self):
        return str(self.__lst[:-1])
        
if __name__ == "__main__":

    numbers_list = [2, 1.5, 34.5, 5.5, 6, 6, 2.4, 5.5, 9]
    
    heap = MinHeap()
    
    for n in numbers_list:
        heap.add(n)
        
    print(heap.peek())
    print(heap.getLst())
    print(f'is it a min heap? {heap.validate()}')


