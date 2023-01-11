# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_sum_ii(root, target_sum):
    all_paths = list()
    current_path = list()

    path_sum_dfs(root, target_sum, current_path, all_paths)

    return all_paths

def path_sum_dfs(current_node, target_sum, current_path, all_paths):
    if current_node is None:
        return 
    
    current_path.append(current_node.value)        

    if current_node.value == target_sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:        
        path_sum_dfs(current_node.left, target_sum - current_node.value, current_path, all_paths)
        path_sum_dfs(current_node.right, target_sum - current_node.value, current_path, all_paths)

    del current_path[-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    target_sum = 23
    print("Tree paths with required_sum " + str(target_sum) + ": " + str(path_sum_ii(root, target_sum)))

main()