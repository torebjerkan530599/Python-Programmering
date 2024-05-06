# An empty tree has a height of -1, a tree with only one node has height 0
from BST import BST

class HeightOfBST(BST):
    def __init__(self):
        self.root = None
        self.size = 0
        
    def height(self):
        return self.heigh_helper(self.root)
    
    def height_helper(self,root):
        if root == None:
            return -1
        else:
            return 1+ max(self.height_helper(root.left), self.height_helper(root.right))
        
if __name__ == "__main__":
    tree = HeightOfBST()
    lst = []
    
        