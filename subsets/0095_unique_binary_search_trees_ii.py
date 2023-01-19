from collections import deque

# Definition for a binary tree node.
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

def unique_binary_search_trees_ii(n):
    if n <= 0:
        return []
    return generate_trees_recursive(1, n)
    
def generate_trees_recursive(start, end):
    unique_binary_search_trees = list()
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end = 1, this means we should have 
    # only one tree we will have two recursive calls, findUniqueTreesRecursive(1, 0) & 
    # (2, 1) both of these should return 'None' for the left and the right child
    if start > end:
        unique_binary_search_trees.append(None)
        return unique_binary_search_trees

    for i in range(start, end + 1):
        # making 'i' the root of the tree
        left_subtrees = generate_trees_recursive(start, i - 1)
        right_subtrees = generate_trees_recursive(i + 1, end)
        # combine all the possible left subtrees with all the 
        # possible right subtrees to generate all possible trees
        # for ecah 'i' as the root of the tree
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                unique_binary_search_trees.append(root)

    return unique_binary_search_trees

def main():
    n = 0
    print("Input: n = " + str(n))
    print("Output: " + str([tree.level_order_traversal() for tree in unique_binary_search_trees_ii(0)]))
    print()

    n = 1
    print("Input: n = " + str(n))
    print("Output: " + str([tree.level_order_traversal() for tree in unique_binary_search_trees_ii(1)]))
    print()

    n = 2
    print("Input: n = " + str(n))
    print("Output: " + str([tree.level_order_traversal() for tree in unique_binary_search_trees_ii(2)]))
    print()
    
    n = 3
    print("Input: n = " + str(n))
    print("Output: " + str([tree.level_order_traversal() for tree in unique_binary_search_trees_ii(3)]))
    print()

main()