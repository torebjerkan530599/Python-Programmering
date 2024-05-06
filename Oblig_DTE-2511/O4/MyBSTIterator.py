from BST import BST

class MyBST(BST):
    def __init__(self):
       BST.__init__(self)
        
    # Return an iterator for a BST
    def __iter__(self):
        return BSTIterator(self.root)
    

class BSTIterator: 
    
    def __init__(self,root):
        self.__stack = []
        self.push_and_go_left(root)
    
    def push_and_go_left(self,node):
        while node:
            self.__stack.append(node)
            node = node.left # smallest value is always leftmost
    
    def __next__(self):
        if not self.__stack:
            raise StopIteration
        
        node = self.__stack.pop()
        if node.right: # in case popped node had a right node
            self.push_and_go_left(node.right) # push right node on stack and go left
            
        return node.element # return element on top of stack

def main():
    tree = MyBST()
    list1 = [8, 3, 1, 9, 2, 5, 12, 8, 3, 1, 9, 2, 5, 12]
    for e in list1:
        tree.insert(e)

    print(str(list1), "are inserted into the tree")
    print("Traverse the elements in this order: ", end = '')
    
    iterator = iter(tree) # Create an iterator
    try:
       while True:
           print(next(iterator), end = ' ')
    except StopIteration:
       print("All traversed")
    
    print("Alternatively use a for loop: ", end = '')
    for e in tree:
        print(e, end=' ')
    
main()