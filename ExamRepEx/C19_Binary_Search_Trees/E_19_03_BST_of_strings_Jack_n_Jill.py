from pathlib import Path

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None



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

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

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

    def get_size(self):
        return self.size
    
    
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

def read_file_and_create_bst(filename):
    bst = BST()
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()
    words = [word.strip(".,;:!?\"").lower() for word in words]
    
    for word in words:
        bst.insert(word)

    return bst

# Main function to run the program
if __name__ == "__main__":
    filepath = Path(__file__).parent / 'JackAndJill.txt'
    bst = read_file_and_create_bst(filepath)
    print(f"The size of the tree is {bst.get_size()}")
    print(bst.search('tumbling'))
    print(bst.search('fumbling'))
    node_path = bst.path('tumbling')
    
    for node in node_path:
       print(node.element)
    
    # alternatively,if i'm totally bonkers...I could do this:   
    #list(map(lambda node: print(node.element), bst.path('tumbling')))
