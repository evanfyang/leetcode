# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_binary_tree_from_array(array, array_length, array_index):
    root = None
    # Base case for recursion 
    if array_index < array_length:
        if array[array_index] == None:
            return root
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
          
    return root

class BSTIterator:
    def __init__(self, root):
        self.stack = list()
        self.traverse_left(root)

    def next(self):
        if self.stack:
            next_node = self.stack.pop()
            self.traverse_left(next_node.right)
            return next_node.value
        else:
            return None

    def has_next(self):
        return bool(self.stack)

    def traverse_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

def main():
    tree = [10,4,15,1,None,14,19,None,None,None,None,None,None,None,20]
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    bst_iterator = BSTIterator(root)
    print("Input: tree = " + str(tree))
    print("has_next: " + str(bst_iterator.has_next())) 
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next())) 
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next()))
    print() 

    tree = [7,3,15,None,None,9,20]
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    bst_iterator = BSTIterator(root)
    print("Input: tree = " + str(tree))
    print("next: " + str(bst_iterator.next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next())) 
    print("next: " + str(bst_iterator.next())) 
    print("has_next: " + str(bst_iterator.has_next())) 
    print()

main()