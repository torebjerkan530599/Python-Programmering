from pathlib import Path


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
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

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

    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

    # Return the node with the smallest value in the tree
    def get_min_node(self):
        current = self.root
        if current is None:
            return None

        while current.left is not None:
            current = current.left

        return current

    # Return the node with the largest value in the tree
    def get_max_node(self):
        current = self.root
        if current is None:
            return None

        while current.right is not None:
            current = current.right

        return current

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


# Test program
def read_file_and_create_bst(filename):
    bst = BST()
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()
    words = [word.strip(".,;:!?\"").lower() for word in words]
    
    for word in words:
        bst.insert(word)

    return bst

if __name__ == "__main__":
    #bst = read_file_and_create_bst("your_text_file.txt")
    filepath = Path(__file__).parent / 'JackAndJill.txt'
    bst = read_file_and_create_bst(filepath)
    min_node = bst.get_min_node()
    max_node = bst.get_max_node()

    if min_node is not None:
        print("Smallest value:", min_node.element)
    else:
        print("The tree is empty.")

    if max_node is not None:
        print("Largest value:", max_node.element)
    else:
        print("The tree is empty.")
