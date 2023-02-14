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
        if array[array_index] is None:
            return root
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
          
    return root

def symmetric_tree(root):
    return root is None or is_symmetric(root.left, root.right)

def is_symmetric(left_subtree, right_subtree):
    if left_subtree is None and right_subtree is None:
        return True
    elif left_subtree is not None and right_subtree is not None:
        return left_subtree.value == right_subtree.value and is_symmetric(left_subtree.left, right_subtree.right) and is_symmetric(left_subtree.right, right_subtree.left)
    else:
        return False
    
def main():
    tree = [1,2,2,3,4,4,3]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(symmetric_tree(root)))
    print()

    tree = [1,2,2,None,3,None,3]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(symmetric_tree(root)))
    print()

    tree = [1]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(symmetric_tree(root)))
    print()

    tree = [None]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(symmetric_tree(root)))
    print()

    tree = [1,2,None]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(symmetric_tree(root)))
    print()

main()