from collections import deque

# Definition for a Node.
class TreeNode:
    def __init__(self, value = 0, left = None, right = None, next = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next
    
    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current_node = next_level_root 
            next_level_root = None
            while current_node:
                print(str(current_node.value) + " ", end='')
                if not next_level_root:
                    if current_node.left:
                        next_level_root = current_node.left
                    if current_node.right:
                        next_level_root = current_node.right
                current_node = current_node.next
            print()
    
    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current_node = self
        while current_node:
            print(str(current_node.value) + " ", end='')
            current_node = current_node.next
        print()

def binary_tree_right_side_view(root):
    right_side_nodes = list()
    
    if root is None:
        return right_side_nodes
    
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current_level_length = len(queue)
        for i in range(current_level_length):
            current_node = queue.popleft()
            if i == current_level_length - 1:
                right_side_nodes.append(current_node.value)
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
    
    return right_side_nodes

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = binary_tree_right_side_view(root)
    print("Tree right view: ", end='')
    for node in result:
        print(str(node) + " ", end='')
    print()

main()