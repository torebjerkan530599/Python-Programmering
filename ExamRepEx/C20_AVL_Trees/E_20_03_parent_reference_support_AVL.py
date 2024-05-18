from BST_with_parent_ref import BST
from BST_with_parent_ref import TreeNode

class AVLTreeNode(TreeNode):
    def __init__(self, e, parent=None):
        self.height = 0
        super().__init__(e, parent)

class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def createNewNode(self, e, parent=None):
        return AVLTreeNode(e, parent)

    def insert(self, e):
        successful = super().insert(e)
        if not successful:
            return False
        else:
            self.balancePath(e)
        return True

    def updateHeight(self, node):
        if node.left is None and node.right is None:
            node.height = 0
        elif node.left is None:
            node.height = 1 + node.right.height
        elif node.right is None:
            node.height = 1 + node.left.height
        else:
            node.height = 1 + max(node.right.height, node.left.height)

    def balancePath(self, e):
        path = self.path(e)
        for i in range(len(path) - 1, -1, -1):
            A = path[i]
            self.updateHeight(A)
            parentOfA = None if A == self.root else path[i - 1]

            if self.balanceFactor(A) == -2:
                if self.balanceFactor(A.left) <= 0:
                    self.balanceLL(A, parentOfA)
                else:
                    self.balanceLR(A, parentOfA)
            elif self.balanceFactor(A) == +2:
                if self.balanceFactor(A.right) >= 0:
                    self.balanceRR(A, parentOfA)
                else:
                    self.balanceRL(A, parentOfA)

    def balanceFactor(self, node):
        if node.right is None:
            return -node.height
        elif node.left is None:
            return node.height
        else:
            return node.right.height - node.left.height

    def balanceLL(self, A, parentOfA):
        B = A.left
        if A == self.root:
            self.root = B
        else:
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B
        A.left = B.right
        if B.right is not None:
            B.right.parent = A
        B.right = A
        B.parent = parentOfA
        A.parent = B
        self.updateHeight(A)
        self.updateHeight(B)

    def balanceLR(self, A, parentOfA):
        B = A.left
        C = B.right
        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
        A.left = C.right
        if C.right is not None:
            C.right.parent = A
        B.right = C.left
        if C.left is not None:
            C.left.parent = B
        C.left = B
        C.right = A
        C.parent = parentOfA
        B.parent = C
        A.parent = C
        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    def balanceRR(self, A, parentOfA):
        B = A.right
        if A == self.root:
            self.root = B
        else:
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B
        A.right = B.left
        if B.left is not None:
            B.left.parent = A
        B.left = A
        B.parent = parentOfA
        A.parent = B
        self.updateHeight(A)
        self.updateHeight(B)

    def balanceRL(self, A, parentOfA):
        B = A.right
        C = B.left
        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
        A.right = C.left
        if C.left is not None:
            C.left.parent = A
        B.left = C.right
        if C.right is not None:
            C.right.parent = B
        C.left = A
        C.right = B
        C.parent = parentOfA
        B.parent = C
        A.parent = C
        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    def delete(self, element):
        node = self.getNode(element)
        if node is None:
            return False
        parent = node.parent
        super().delete(element)
        while parent is not None:
            self.updateHeight(parent)
            if self.balanceFactor(parent) == -2:
                if self.balanceFactor(parent.left) <= 0:
                    self.balanceLL(parent, parent.parent)
                else:
                    self.balanceLR(parent, parent.parent)
            elif self.balanceFactor(parent) == +2:
                if self.balanceFactor(parent.right) >= 0:
                    self.balanceRR(parent, parent.parent)
                else:
                    self.balanceRL(parent, parent.parent)
            parent = parent.parent
        return True

# Test program
if __name__ == "__main__":
    avl_tree = AVLTree()
    numbers = list(range(1, 101))

    # Insert numbers 1 to 100
    for num in numbers:
        avl_tree.insert(num)

    # Display paths for all leaf nodes
    for num in numbers:
        if avl_tree.isLeaf(num):
            print(f"Path for {num}: {avl_tree.getPath(num)}")
