from BST import BST

class MyBST(BST):
    def __init__(self):
        BST.__init__(self)
        
    # Returns the number of nonleaf nodes 
    def getNumberofNonLeaves(self):
        return self.size - self.getNumberOfLeaves()

    # Returns the number of leaf nodes 
    def getNumberOfLeaves(self):
        return self.getNumberOfLeaves1(self.root)
    
    # Returns the number of leaf nodes 
    def getNumberOfLeaves1(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return self.getNumberOfLeaves1(root.left) + self.getNumberOfLeaves1(root.right)

def main():
    tree = MyBST()
    print("The number of nonleaves in an empty tree is", tree.getNumberofNonLeaves())

    s = input("Enter integers in one line for tree separated by comma: ")
    # 50,30,70,20,40,60,80,10,35,65
    # 50 30 70 20 40 60 80 10 35 65
    lst = [int(x) for x in s.split(',')]
    for e in lst:
        tree.insert(e)
        
    print(s, "are inserted into the tree")
    print("The number of nonleaves in the tree is", tree.getNumberofNonLeaves())
    
main()
