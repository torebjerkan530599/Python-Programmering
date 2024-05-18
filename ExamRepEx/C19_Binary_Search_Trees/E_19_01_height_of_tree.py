# An empty tree has a height of -1, a tree with only one node has height 0
from BST import BST

class HeightOfBST():        
    def height(self,root):
        if root == None:
            return -1
        else:
            return 1+ max(self.height(root.left), self.height(root.right))
        
if __name__ == "__main__":
    bst = BST()
    lst = [65,21,46,33,77,11,15,66,43,25,86]
    
    for e in lst:
        bst.insert(e)
    
    tree = HeightOfBST()
    
    print(tree.height(bst.root))
    

    
        