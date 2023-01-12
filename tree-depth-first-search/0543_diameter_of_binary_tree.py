# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def diameter_of_binary_tree_grokking(root):
    max_diameter = 0
    
    def find_max_diameter_dfs(current_node):
        nonlocal max_diameter

        if current_node is None:
            return 0
        
        left_subtree_height = find_max_diameter_dfs(current_node.left)
        right_subtree_height = find_max_diameter_dfs(current_node.right)

        if left_subtree_height != 0 and right_subtree_height != 0:
            diameter = left_subtree_height + right_subtree_height + 1
            max_diameter = max(max_diameter, diameter)
        
        return max(left_subtree_height, right_subtree_height) + 1
    
    find_max_diameter_dfs(root)
    return max_diameter

def diameter_of_binary_tree(root):
    max_diameter = 0
    
    def find_max_diameter_dfs(current_node):
        nonlocal max_diameter

        if current_node is None:
            return -1
        
        left_subtree_height = find_max_diameter_dfs(current_node.left)
        right_subtree_height = find_max_diameter_dfs(current_node.right)
        
        max_diameter = max(max_diameter, left_subtree_height + right_subtree_height + 2)
        return max(left_subtree_height, right_subtree_height) + 1
    
    find_max_diameter_dfs(root)
    return max_diameter

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(diameter_of_binary_tree(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(diameter_of_binary_tree(root))) 

main()