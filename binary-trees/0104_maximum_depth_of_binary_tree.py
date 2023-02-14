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

def maximum_depth_of_binary_tree(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return 1 + max(maximum_depth_of_binary_tree(root.left), maximum_depth_of_binary_tree(root.right))

def main():
    tree = [3,9,20,None,None,15,7]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(maximum_depth_of_binary_tree(root)))
    print()

    tree = [1,None,2]
    print("Input: tree = " + str(tree))
    root = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(maximum_depth_of_binary_tree(root)))
    print()

main()