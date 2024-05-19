class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getHead(self):
        if self.__size == 0:
            return None
        else:
            return self.__head

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e

        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node

        self.__size += 1 # Increase size


    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            current.next.next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result


    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0


    # Return true if this list contains the element o 
    def contains(self, e):
        current = self.__head
        for i in range(self.__size):
            if(current.element == e):
                return True     
            current = current.next
        return False

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        if self.__head is None:
            return False  # List is empty
        
        if(self.__head.element == e):
            return self.removeFirst() 
             
        current = self.__head 
        while current.next is not None:
            if(current.next.element == e):          
                current.next = current.next.next
                self.__size -= 1
                return True
            current = current.next
        return False

    # Return the element from this list at the specified index 
    def get(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.__head.element # return head 
        elif index == self.__size - 1:
            return self.__tail.element # return tail
        else:
            current = self.__head
            for i in range(1, index+1):
                current = current.next
                if( i == index):
                    return current.element
        return None
                
    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        current = self.__head
        for i in range(self.__size):
            if(current.element == e):
                return i
            current = current.next
        return -1
    
    # Last index of the specified element in this list
    def lastIndexOf(self, e):
        index = -1
        current = self.__head
        for i in range(self.__size):
            if current.element == e:
                index = i
            current = current.next
        return index

    # Set the element at the specified position in this list
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return False  # Index out of range
        elif index == 0:
            new_node = Node(e)
            new_node.next = self.__head.next
            self.__head = new_node
            return True
        else:
            current = self.__head
            for i in range(index):
                current = current.next
            current.element = e
            return True


    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)


# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    



class MyLinkedList(LinkedList):
    # Add the elements in otherList to this list. 
    # Return True if this list changed as a result of the call 
    def addAll(self, otherList):
        changed = False
        current = otherList.getHead()
        while current is not None:
            #if not self.contains(current.element):  # Add only if element does not exist
                self.addLast(current.element)
                changed = True
                current = current.next
        return changed

    def removeAll(self, otherList):
        changed = False
        current = otherList.getHead()
        while current is not None:
            while self.contains(current.element):  # Remove all occurrences
                self.remove(current.element)
                changed = True
            current = current.next
        return changed

    def retainAll(self, otherList):
        changed = False
        current = self.getHead()
        while current is not None:
            if not otherList.contains(current.element):  
                while self.contains(current.element):  # Remove all occurrences
                    self.remove(current.element)
                    changed = True
            current = current.next
        return changed



# Test code
def main():
    
    lista = ['red', 'green', 'red', 'black' ]#input("Enter list1: ").split()
    listb = ['red', 'black', 'yellow']#input("Enter list2: ").split() 
    
    list1 = MyLinkedList()
    list2 = MyLinkedList()
    for s in lista:
        list1.add(s)
    for s in listb:
        list2.add(s)
    
    list1.addAll(list2)
    print("After list1.addAll(list2), list1 is", list1)
    
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    list1.removeAll(list2)
    print("After list1.removeAll(list2), list1 is", list1)

    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    list1.retainAll(list2)
    print("After list1.retainAll(list2), list1 is", list1)
    
main()
