class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        while current is not None:
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
        if self.root is None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current is not None:
                parent = current
                if e < current.element:
                    current = current.left
                elif e > current.element:
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            newNode = self.createNewNode(e)
            newNode.parent = parent
            if e < parent.element:
                parent.left = newNode
            else:
                parent.right = newNode

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
        if r is not None:
            self.inorderHelper(r.left)
            print(r.element, end=" ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root is not None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end=" ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root is not None:
            print(root.element, end=" ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current is not None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current is not None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current is None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left is None:
            if parent is None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
                if current.right is not None:
                    current.right.parent = parent
        else:
            # Case 2: The current node has a left child
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right is not None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
                if rightMost.left is not None:
                    rightMost.left.parent = parentOfRightMost
            else:
                parentOfRightMost.left = rightMost.left
                if rightMost.left is not None:
                    rightMost.left.parent = parentOfRightMost

        self.size -= 1
        return True # Element deleted

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

    # Return the node for the specified element.
    # Return None if the element is not in the tree.
    def getNode(self, element):
        current = self.root
        while current is not None:
            if element < current.element:
                current = current.left
            elif element > current.element:
                current = current.right
            else:
                return current
        return None

    # Return True if the node for the element is a leaf
    def isLeaf(self, element):
        node = self.getNode(element)
        if node is None:
            return False
        return node.left is None and node.right is None

    # Return the path of elements from the specified element
    # to the root in a list.
    def getPath(self, e):
        path = []
        node = self.getNode(e)
        while node is not None:
            path.append(node.element)
            node = node.parent
        return path

class TreeNode:
    def __init__(self, e, parent=None):
        self.element = e
        self.left = None
        self.right = None
        self.parent = parent

# Test program
if __name__ == "__main__":
    tree = BST()
    a_list = [50,30,70,20,40,60,80,10,35,65]
    #values = list(map(int, a_list.split(',')))

    for value in a_list:
        tree.insert(value)

    # Delete the first integer from the tree
    tree.delete(a_list[0])

    # Display the paths for each leaf node to the root
    print("Paths from leaf nodes to the root:")
    for value in a_list:
        if tree.isLeaf(value):
            print(f"Path for {value}: {tree.getPath(value)}")
