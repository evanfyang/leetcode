from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_successor(root, key):        
    successor = None
    
    if root is None:
        return successor

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.popleft()
        
        if current_node.left is not None:
            queue.append(current_node.left)
        
        if current_node.right is not None:
            queue.append(current_node.right)
        
        if current_node.value == key:
            break
    
    if len(queue) > 0:
        successor = queue.popleft()
    
    return successor

def main():
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left = TreeNode(4);
    root.left.right = TreeNode(5);
    
    result = level_order_successor(root, 3)
    if result:
        print(result.value)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    result = level_order_successor(root, 9)
    if result:
        print(result.value)
    
    result = level_order_successor(root, 12)
    if result:
        print(result.value)

main()