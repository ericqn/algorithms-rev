import numpy as np

class BST_Node:
    def __init__(self, value):
        assert type(value) == int
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        """Insert to left child with value specified"""
        self.left = BST_Node(value)
    
    def insert_right(self, value):
        """Insert to right child with value specified"""
        self.right = BST_Node(value)
    
    def is_leaf(self) -> bool:
        """Determines if node is a leaf node (has no children)"""
        return (not self.left) and (not self.right)

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f'Node Value: {self.value}'


class BST:
    def __init__(self, root=None):
        if root:
            self.root = BST_Node(value=root)
        else:
            self.root = None

    def insert(self, value):
        """Inserts node starting from the root."""
        def insert_helper(value, curr_node:BST_Node=None):
            if not curr_node:
                curr_node = BST_Node(value)
                print('Base Case')
                return
            
            if value < curr_node.value and curr_node.left:
                return insert_helper(value, curr_node.left)
            elif value < curr_node.value and not curr_node.left:
                curr_node.insert_left(value)
                print('Inserted Node!')
                return
            elif value > curr_node.value and curr_node.right:
                return insert_helper(value, curr_node.right)
            elif value > curr_node.value and not curr_node.right:
                curr_node.insert_right(value)
                print('Inserted Node!')
                return
            else:
                print('Duplicate node values found.')
                return
        
        insert_helper(value, curr_node=self.root)
        
    
    def inorder_traversal(self, curr_node:BST_Node=None):
        if curr_node is None:
            return 
        
        self.inorder_traversal(curr_node.left)
        print(curr_node)
        self.inorder_traversal(curr_node.right)

if __name__ == '__main__':
    print('===== BINARY TREE TESTING =====')
    node1 = BST_Node(3)
    node2 = BST_Node(7)
    node1.insert_left(4)

    print(node1)
    print(node1 < node2)
    print(node1 == node2)
    print(node1.is_leaf())

    bst = BST(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)
    bst.insert(1)
    # print(bst.root.left)
    # print(bst.root.right)
    print(bst.inorder_traversal(curr_node=bst.root))