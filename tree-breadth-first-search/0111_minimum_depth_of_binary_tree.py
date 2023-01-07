from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimum_depth_of_binary_tree(root):
    minimum_depth = 0
    
    if root is None:
        return minimum_depth
    
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        minimum_depth += 1
        current_level_length = len(queue)
        for _ in range(current_level_length):
            current_node = queue.popleft()

            if current_node.left is None and current_node.right is None:
                return minimum_depth

            if current_node.left is not None: 
                queue.append(current_node.left)
            if current_node.right is not None: 
                queue.append(current_node.right)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(minimum_depth_of_binary_tree(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(minimum_depth_of_binary_tree(root)))

main()