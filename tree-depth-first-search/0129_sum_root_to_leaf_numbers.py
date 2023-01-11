# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def sum_root_to_leaf_numbers(root):
    path_sum = 0
    return sum_root_to_leaf_dfs(root, path_sum)

def sum_root_to_leaf_dfs(current_node, path_sum):
    if current_node is None:
        return 0
    
    path_sum = 10 * path_sum + current_node.value

    if current_node.left is None and current_node.right is None:
        return path_sum

    return sum_root_to_leaf_dfs(current_node.left, path_sum) + sum_root_to_leaf_dfs(current_node.right, path_sum)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(sum_root_to_leaf_numbers(root)))

main()