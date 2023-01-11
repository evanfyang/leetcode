# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_with_given_sequence(root, sequence):
    index = 0
    return check_paths_dfs(root, sequence, index)

def check_paths_dfs(current_node, sequence, index):
    if current_node is None:
        return False
    
    sequence_length = len(sequence)

    if index >= sequence_length or current_node.value != sequence[index]:
        return False
    
    if current_node.left is None and current_node.right is None and index == sequence_length - 1:
        return True
    
    return check_paths_dfs(current_node.left, sequence, index + 1) or check_paths_dfs(current_node.right, sequence, index + 1)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(path_with_given_sequence(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(path_with_given_sequence(root, [1, 1, 6])))

main()

