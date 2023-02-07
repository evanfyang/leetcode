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

def balanced_binary_tree(root):
    def dfs(root):
        if root is None: 
            return [True, 0]

        left_subtree, right_subtree = dfs(root.left), dfs(root.right)
        balanced = left_subtree[0] and right_subtree[0] and abs(left_subtree[1] - right_subtree[1]) <= 1

        return [balanced, 1 + max(left_subtree[1], right_subtree[1])]
    
    return dfs(root)[0]

def main():
    tree = [3,9,20,None,None,15,7]
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(balanced_binary_tree(tree))) 
    print()

    tree = [1,2,2,3,3,None,None,4,4]
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(balanced_binary_tree(tree))) 
    print()

    tree = []
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(balanced_binary_tree(tree))) 
    print()

main()