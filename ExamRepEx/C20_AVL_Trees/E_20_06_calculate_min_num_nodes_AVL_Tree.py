class TreeNode:
    def __init__(self, e, parent=None):
        self.element = e
        self.left = None
        self.right = None
        self.parent = parent

class AVLTreeNode(TreeNode):
    def __init__(self, e, parent=None):
        super().__init__(e, parent)
        self.height = 0
        self.size = 1

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def createNewNode(self, e, parent=None):
        return TreeNode(e, parent)

    def insert(self, e):
        if self.root is None:
            self.root = self.createNewNode(e)
        else:
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
                    return False

            if e < parent.element:
                parent.left = self.createNewNode(e, parent)
            else:
                parent.right = self.createNewNode(e, parent)

        self.size += 1
        return True

    def path(self, e):
        path = []
        current = self.root
        while current is not None:
            path.append(current)
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break
        return path

class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def createNewNode(self, e, parent=None):
        return AVLTreeNode(e, parent)

    def insert(self, e):
        if self.root is None:
            self.root = self.createNewNode(e)
        else:
            self.root = self.insert_node(self.root, e)

        self.size += 1
        return True

    def insert_node(self, node, e):
        if node is None:
            return self.createNewNode(e)

        if e < node.element:
            node.left = self.insert_node(node.left, e)
            node.left.parent = node
        elif e > node.element:
            node.right = self.insert_node(node.right, e)
            node.right.parent = node
        else:
            return node

        self.updateHeight(node)
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
        return self.balance(node)

    def updateHeight(self, node):
        if node.left is None and node.right is None:
            node.height = 0
        elif node.left is None:
            node.height = 1 + node.right.height
        elif node.right is None:
            node.height = 1 + node.left.height
        else:
            node.height = 1 + max(node.left.height, node.right.height)

    def balance(self, node):
        balance_factor = self.getBalanceFactor(node)
        if balance_factor == -2:
            if self.getBalanceFactor(node.left) <= 0:
                return self.balanceLL(node)
            else:
                return self.balanceLR(node)
        elif balance_factor == 2:
            if self.getBalanceFactor(node.right) >= 0:
                return self.balanceRR(node)
            else:
                return self.balanceRL(node)
        return node

    def getBalanceFactor(self, node):
        if node.right is None:
            return -node.height
        elif node.left is None:
            return node.height
        else:
            return node.right.height - node.left.height

    def balanceLL(self, A):
        B = A.left
        A.left = B.right
        if B.right is not None:
            B.right.parent = A
        B.right = A
        A.parent = B
        self.updateHeight(A)
        self.updateHeight(B)
        A.size = 1 + (A.left.size if A.left else 0) + (A.right.size if A.right else 0)
        B.size = 1 + (B.left.size if B.left else 0) + (B.right.size if B.right else 0)
        return B

    def balanceLR(self, A):
        A.left = self.balanceRR(A.left)
        return self.balanceLL(A)

    def balanceRR(self, A):
        B = A.right
        A.right = B.left
        if B.left is not None:
            B.left.parent = A
        B.left = A
        A.parent = B
        self.updateHeight(A)
        self.updateHeight(B)
        A.size = 1 + (A.left.size if A.left else 0) + (A.right.size if A.right else 0)
        B.size = 1 + (B.left.size if B.left else 0) + (B.right.size if B.right else 0)
        return B

    def balanceRL(self, A):
        A.right = self.balanceLL(A.right)
        return self.balanceRR(A)

    def find(self, k):
        if k < 1 or k > (self.root.size if self.root else 0):
            return None
        return self._find(k, self.root)

    def _find(self, k, root):
        if root is None:
            return None

        left_size = root.left.size if root.left else 0
        if k <= left_size:
            return self._find(k, root.left)
        elif k == left_size + 1:
            return root.element
        else:
            return self._find(k - left_size - 1, root.right)
    
    # static
    def min_nodes(height, memo=None):
        if memo is None:
            memo = {}

        # Base cases
        if height == 0:
            return 1
        if height == 1:
            return 2

        # Check if result is already computed
        if height in memo:
            return memo[height]

        # Recursive calculation
        result = 1 + AVLTree.min_nodes(height - 1, memo) + AVLTree.min_nodes(height - 2, memo)
        memo[height] = result
        return result
'''
iterative simulation of tail recursion
def min_nodes(height):
    if height == 0:
        return 1
    if height == 1:
        return 2
    
    prev = 1
    curr = 2
    for _ in range(2, height + 1):
        next_val = 1 + prev + curr
        prev, curr = curr, next_val
    
    return curr

'''

# Test program
if __name__ == "__main__":
    while True:
        try:
            height = int(input("Enter the height of the AVL tree: "))
            if height < 0:
                print("Height cannot be negative. Please enter a non-negative integer.")
                continue
            result = AVLTree.min_nodes(height)
            print(f"The minimum number of nodes required for an AVL tree of height {height} is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
