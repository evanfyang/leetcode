# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_sum(root, target_sum):
    if root is None:
        return False

    if root.value == target_sum and root.left is None and root.right is None:
        return True
    
    return path_sum(root.left, target_sum - root.value) or path_sum(root.right, target_sum - root.value)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(path_sum(root, 23)))
    print("Tree has path: " + str(path_sum(root, 16)))

main()