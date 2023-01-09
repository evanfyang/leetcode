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

def populating_next_right_pointers_in_each_node(root):
    if root is None:
        return root

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current_level_length = len(queue)
        for i in range(current_level_length):
            current_node = queue.popleft()
            if i + 1 < current_level_length:
                current_node.next = queue[0]
            else:
                current_node.next = None

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return root

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    populating_next_right_pointers_in_each_node(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()

main()
