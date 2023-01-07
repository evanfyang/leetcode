from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_level_order_traversal(root):        
    traversal = list()
            
    if root is None:
        return traversal 

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current_level = list()
        current_level_length = len(queue)
        
        for _ in range(current_level_length):
            current_node = queue.popleft()
            current_level.append(current_node.value)
            
            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)
        
        traversal.append(current_level)
    
    return traversal

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(binary_tree_level_order_traversal(root)))

main()