# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_sum_iii(root, target_sum):
    prefix_sum_frequency = dict()
    return count_paths_prefix_sum_dfs(root, target_sum, prefix_sum_frequency, 0)

def count_paths_prefix_sum_dfs(current_node, target_sum, prefix_sum_frequency, current_path_sum):
    if current_node is None:
        return 0
    
    path_count = 0
    current_path_sum += current_node.value
    
    if current_path_sum == target_sum:
        path_count += 1
    
    path_count += prefix_sum_frequency.get(current_path_sum - target_sum, 0)
    prefix_sum_frequency[current_path_sum] = prefix_sum_frequency.get(current_path_sum, 0) + 1

    path_count += count_paths_prefix_sum_dfs(current_node.left, target_sum, prefix_sum_frequency, current_path_sum)
    path_count += count_paths_prefix_sum_dfs(current_node.right, target_sum, prefix_sum_frequency, current_path_sum)

    prefix_sum_frequency[current_path_sum] = prefix_sum_frequency.get(current_path_sum, 1) - 1

    return path_count

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(path_sum_iii(root, 11)))

main()