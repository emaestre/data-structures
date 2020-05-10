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

    def find_inorder_successor(self, bst_node):
        current = bst_node
        while current.left:
            current = current.left
        return current
    
    def remove(self, bst_node, element):
        if not bst_node: 
            return bst_node  
    
        if element < bst_node.value: 
            bst_node.left = self.remove(bst_node.left, element) 
        elif(element > bst_node.value): 
            bst_node.right = self.remove(bst_node.right, element) 
        else: 
            if not bst_node.left: 
                temp = bst_node.right  
                bst_node = None 
                return temp
            
            if not bst_node.right: 
                temp = bst_node.left  
                bst_node = None
                return temp 
     
            temp = self.find_inorder_successor(bst_node.right) 
    
            bst_node.value = temp.value 
            bst_node.right = self.remove(bst_node.right, temp.value) 
    
        return bst_node

# Container tree class
class BST:
    def __init__(self):
        self.root = None

    def preorder(self):
        if self.root:
            self.root.preorder()
        print()

    def insert(self, new_val):
        if self.root:
            self.root.insert(new_val)
        else:
            self.root = BST_Node(new_val)

    def search(self, element):
        if self.root:
            return self.root.search(element)

        return False

    def remove(self, element):
        if self.root:
            return self.root.remove(self.root, element)
        
        return self.root


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
    tree.remove(4)
    tree.preorder()
