from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def level_order_traversal(self):
        traversal = list()
        
        if self is None:
            return traversal 

        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current_level = list()
            current_level_length = len(queue)
            
            for _ in range(current_level_length):
                current_node = queue.popleft()
                if current_node is not None:
                    current_level.append(current_node.value)
                else:
                    current_level.append(None)
                    continue
                    
                if current_node.left is None and current_node.right is None:
                    continue
                
                if current_node.left is not None:
                    queue.append(current_node.left)
                else:
                    queue.append(None)
                
                if current_node.right is not None:
                    queue.append(current_node.right)
                else:
                    queue.append(None)
            
            for node_values in current_level:
                traversal.append(node_values)
        
        return traversal

def generate_binary_tree_from_array(array, array_length, array_index):
    root = None
    # Base case for recursion 
    if array_index < array_length:
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
          
    return root

def invert_binary_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

def main():
    tree = [10,4,15,1,None,14,19,None,None,None,None,None,None,None,20]
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    inverted_tree = invert_binary_tree(tree)
    print("Output: " + str(inverted_tree.level_order_traversal() if inverted_tree else []))
    print()

    tree = [4,2,7,1,3,6,9]
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    inverted_tree = invert_binary_tree(tree)
    print("Output: inverted_tree = " + str(inverted_tree.level_order_traversal() if inverted_tree else []))
    print()

    tree = [2,1,3]
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    inverted_tree = invert_binary_tree(tree)
    print("Output: inverted_tree = " + str(inverted_tree.level_order_traversal() if inverted_tree else []))
    print()

    tree = []
    print("Input: tree = " + str(tree))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    inverted_tree = invert_binary_tree(tree)
    print("Output: inverted_tree = " + str(inverted_tree.level_order_traversal() if inverted_tree else []))
    print()

main()