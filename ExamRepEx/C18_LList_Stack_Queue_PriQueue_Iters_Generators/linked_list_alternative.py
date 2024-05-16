
class MyNode:

    def __init__(self, content, previous_node=None, next_node=None):
        self.content = content
        self.previous_node = previous_node
        self.next_node = next_node

    def setNext(self, next_node):
        self.next_node = next_node

    def setPrevious(self, prev_node):
        self.previous_node = prev_node

    def getContent(self):
        return self.content
    
class MyLinkedList:

    def __init__(self, data):
        self.list_length = len(data)  # number of elements in the list (the length itself is not 0 index based)
        self.data = data
        self.first_node = None
        self.last_node = None
        self.item = None

        # build the initial list out of the data if data is provided
        for d in data:
            new_node = MyNode(d)
            if self.first_node is None:
                self.first_node = new_node
            if self.last_node is None:
                self.last_node = new_node
            else:
                new_node.setPrevious(self.last_node)  # last.node is previous new_node so update the it's setPrevious()
                self.last_node.setNext(new_node)  # last.node is previous new_node so update the it's setNext()
                self.last_node = new_node  # move last pointer up the chain

    def __getitem__(self, idx):
        if self.first_node is None:
            return None

        if idx > self.list_length:
            return "Not an valid index"

        search_node = self.first_node
        self.item = search_node.getContent()

        if idx > 0:
            for i in range(0, idx):
                if search_node.next_node is not None:
                    search_node = search_node.next_node
                    self.item = search_node.getContent()
                else:
                    return "Not an valid index"

        return self.item

    def __setitem__(self, idx, item):
        pass

    def __add__(self, my_list):
        pass

    def __delitem__(self, idx):
        if self.first_node is None:
            return None

        if idx > self.list_length - 1:
            return "Not an valid index"

        # special case of deleting the first item
        if idx == 0:
            self.first_node = self.first_node.next_node  # overwrite
            self.first_node.setPrevious = None
            return "first item was deleted"

        # special case of deleting the last item
        if idx == self.list_length - 1:
            self.last_node = self.last_node.previous_node  # overwrite
            self.last_node.setNext(None)
            return "last item was deleted"

        search_node = self.first_node
        for i in range(1, idx+1):  # starts from 1 because we already checked index 0. 1 is inclusive. index is not.:

            if i == idx:
                prev = search_node.previous_node
                prev.setNext(search_node.next_node)  # link past the node to be deleted
                item = search_node.getContent()
                # del search_node  # this is the way to delete any reference to the node...right? But should I use none?
                # I could just link around it and forget about it since it is no longer in the linked list?
                return item
            elif search_node.next_node is not None:
                search_node = search_node.next_node
                print('still searching...')

        self.list_length -= 1  # reduce the list by one entry

    def __eq__(self, my_list):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        return self.list_length

    def __contains__(self, item):
        pass

    def __str__(self):
        node = self.first_node
        while node is not None:
            print(node.getContent())
            node = node.next_node

    def append(self, item):
        new_node = MyNode(item)
        if self.first_node is None:
            self.first_node = new_node
        if self.last_node is None:
            self.last_node = new_node
        else:
            new_node.setPrevious(self.last_node)  # last.node is previous new_node so update the it's setPrevious()
            self.last_node.setNext(new_node)  # last.node is previous new_node so update the it's setNext()
            self.last_node = new_node  # move last pointer up the chain

        self.list_length += 1  # update the length of the list by one

    def insert(self, idx, item):

        new_node = MyNode(item)

        # special case of inserting a new first item
        if idx == 0:
            new_node.setNext(self.first_node)  # new_node.previous is automatically set to None
            self.first_node.setPrevious(new_node)
            self.first_node = new_node

        # special case of inserting at the end of the list
        elif idx == self.list_length - 1:
            new_node.setPrevious(self.last_node)
            self.last_node.setNext(new_node)
            self.last_node = new_node

        else:
            # index = idx + 1  # adjust the index because the range function doesn't include the last index provided
            search_node = self.first_node

            for i in range(1, idx+1):  # from 1 because we already checked index 0. +1 because idx is non-inclusive
                if i == idx:
                    new_node.setPrevious(search_node)
                    new_node.setNext(search_node.next_node)
                    search_node.setNext(new_node)
                elif search_node.next_node is not None:
                    search_node = search_node.next_node

        self.list_length += 1


if __name__ == "__main__":
    person_01 = 'Anders'
    person_02 = 'Bjarne'
    person_03 = 'Cato'
    person_04 = 'David'

    persons_list = [person_01, person_02, person_03, person_04]

    x = MyLinkedList(persons_list)

    print(f'\nAppending Eirik to the list\n')
    x.append('Eirik')
    x.__str__()

    index = int(input("\nwhich index would you like retrieve? (-1 for quit) "))

    while index != -1:
        print(f'retrieving index {index}: {x.__getitem__(index)} \n')
        index = int(input("which index would you like retrieve? (-1 for quit) "))

    print('\nDeleting third item\n')
    report = x.__delitem__(3)  # deleting the head

    print(f'\n{report} was deleted \n')

    x.__str__()

    new_item = 'Alfred'
    print(f'\nInserting {new_item} at the beginning of the list:\n')
    x.insert(0, new_item)

    print()
    x.__str__()

    new_item = 'Fred'
    print(f'\nInserting {new_item} at the end of the list:\n')
    x.insert(x.list_length-1, new_item)

    print()
    x.__str__()

    new_item = 'Birger'
    index = 3
    print(f'\nInserting {new_item} at index {index} in the list:\n')
    x.insert(index, new_item)



    print()
    x.__str__()