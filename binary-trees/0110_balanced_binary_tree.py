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
        # base case: when current root of tree is None, return True
        # for balanced and height of 0
        if root is None: 
            return [True, 0]

        # check if right and left subtree are balanced and get their heights
        left_subtree, right_subtree = dfs(root.left), dfs(root.right)
        # check if the tree at the current root is balanced by checking if 
        # both left and right subtree are balanced and if the difference in 
        # height between the left and right subtree is equal to or less than 1
        balanced = left_subtree[0] and right_subtree[0] and abs(left_subtree[1] - right_subtree[1]) <= 1

        # return if the tree at the current root is balanced and the height
        # of the tree at the current root; height of the tree at the current 
        # root is calculated by taking the max height of the two subtrees and 
        # adding one to account for the root
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