class BST_Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def preorder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def insert(self, new_val):
        # Duplicates are not wanted
        if self.value != new_val:
            if new_val < self.value:
                if self.left:
                    self.left.insert(new_val)
                else:
                    self.left = BST_Node(new_val)
            else:
                if self.right:
                    self.right.insert(new_val)
                else:
                    self.right = BST_Node(new_val)

    def search(self, element):
        if self.value == element:
            return True

        if element < self.value and self.left:
            return self.left.search(element)

        if element > self.value and self.right:
            return self.right.search(element)

        return False


# Container tree class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_val):
        if self.root:
            self.root.insert(new_val)
        else:
            self.root = BST_Node(new_val)

    def preorder(self):
        if self.root:
            self.root.preorder()
        print()

    def search(self, element):
        if self.root:
            return self.root.search(element)

        return False


if __name__ == "__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(6)
    tree.insert(1)
    tree.insert(2)
    tree.preorder()
    print(tree.search(10))
    print(tree.search(6))
    print(tree.search(2))
