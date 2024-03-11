class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

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
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
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
        current = self.__head 
        for i in range(self.__size):
            current = current.next
            if(current.next.element == e):          
                current.next = current.next.next
                self.__size -= 1
                return True
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

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        for i in range(self.__size,0,-1):
            other_e = self.get(i)
            if(other_e == e):
                return i
        return -1

    # Replace the element at the specified position in this list
    #  with the specified element. */      
    def set(self, index, e):
        current = self.__head
        prev = None
        for i in range(self.__size):
            if i == index:
                new_node = Node(e)
                if prev:
                    prev.next = new_node
                else:
                    self.__head = new_node
                new_node.next = current.next
                del current
                return True
            prev = current
            current = current.next
        return False
    
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


def main():
    linked_list = LinkedList()
    text_string = "There was a time when everything was all sweet and dandy"
    text_array = text_string.split()
    
    #add words in text_array to linked_list
    for word in text_array:
        linked_list.add(word)
    
    print(linked_list)
        
    #test contains(e) function:
    test_string =["sweet","home","alabama"]
    
    for word in test_string:
        print(f'It is {linked_list.contains(word)} that the linked list contains the word \"{word}\"')

    # test get from index method:
    print(f'{linked_list.get(3)} == time')
    
    test_word = "was"
    print(f'first occurence of \"{test_word}\" at index {linked_list.indexOf(test_word)}')
    print()
    print(f'last occurence of \"{test_word}\" at index {linked_list.lastIndexOf(test_word)}')

    linked_list.remove('all')
    print("after invoking linked_list.remove('all'), linked_list is", linked_list)
    
    index = 3
    linked_list.set(index, "orange")
    print("after invoking linked_list.set('" + str(index) + " , orange)", "linked_list is", linked_list)
    
main()