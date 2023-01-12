import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_maximum_path_sum(root):
    global_max_path_sum = -math.inf
    
    def find_max_path_sum_dfs(current_node):
        nonlocal global_max_path_sum
        
        if current_node is None:
            return 0
        
        max_path_sum_left = find_max_path_sum_dfs(current_node.left)
        max_path_sum_right = find_max_path_sum_dfs(current_node.right)

        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        max_path_sum_left = max(max_path_sum_left, 0)
        max_path_sum_right = max(max_path_sum_right, 0)

        # maximum path sum at the current node will be equal to the sum from the left 
        # subtree + the sum from right subtree + val of current node
        local_max_path_sum = max_path_sum_left + max_path_sum_right + current_node.value
        
        # update the global maximum sum
        global_max_path_sum = max(global_max_path_sum, local_max_path_sum)

        return max(max_path_sum_left, max_path_sum_right) + current_node.value
    
    find_max_path_sum_dfs(root)
    return global_max_path_sum[0]

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: " + str(binary_tree_maximum_path_sum(root)))
    
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(binary_tree_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(binary_tree_maximum_path_sum(root)))

main()