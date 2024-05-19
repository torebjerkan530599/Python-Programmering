class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    # Inorder traversal from the root
    def inorder(self):
        if not self.root:
            return
        stack = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.element, end=" ")
            current = current.right

    # Postorder traversal from the root 
    def postorder(self):
        if not self.root:
            return
        stack1 = []
        stack2 = []
        stack1.append(self.root)

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.element, end=" ")

    # Preorder traversal from the root 
    # def preorder(self):
    #     self.preorderHelper(self.root)

    # # Preorder traversal from a subtree 
    # def preorderHelper(self, root):
    #     if root != None:
    #         print(root.element, end = " ")
    #         self.preorderHelper(root.left)
    #         self.preorderHelper(root.right)
    
    def preorder(self):
        if not self.root:
            return
        stack = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            print(node.element, end=" ")

            # Push right and then left child to stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None

# Example usage
if __name__ == "__main__":
    bst = BST()
    bst.insert(40)
    bst.insert(20)
    bst.insert(60)
    bst.insert(10)
    bst.insert(30)
    bst.insert(50)
    bst.insert(70)

    print("Inorder traversal:", end=' ')
    bst.inorder()
    print()
    print('Preorder traversal:', end=' ')
    bst.preorder()
    print()
    print('Postorder traversal:', end=' ')
    bst.postorder()
