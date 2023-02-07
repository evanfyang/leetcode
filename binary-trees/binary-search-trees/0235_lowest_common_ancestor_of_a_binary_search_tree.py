# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_binary_tree_from_array(array, array_length, array_index):
    root = None
    # Base case for recursion 
    if array_index < array_length:
        if array[array_index] == None:
            return root
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
    
    return root

def lowest_common_ancestor_of_a_binary_search_tree(root, p, q):
    current_node = root
    while current_node is not None:
        if current_node.value < p.value and current_node.value < q.value:
            current_node = current_node.right
        elif current_node.value > p.value and current_node.value > q.value:
            current_node = current_node.left
        else:
            return current_node
            '''
            this else block covers these conditions:
            if current_node.value < p.value and current_node.value > q.value:
                return current_node
            if current_node.value > p.value and current_node.value < q.value:
                return current_node
            if current_node.value == p.value:
                return current_node
            if current_node.value == q.value:
                return current_node
            '''

def main():
    tree = [6,2,8,0,4,7,9,None,None,3,5]
    p = TreeNode(2)
    q = TreeNode(8)
    print("Input: tree = " + str(tree) + ", p = " + str(p.value) + ", q = " + str(q.value))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(lowest_common_ancestor_of_a_binary_search_tree(tree, p, q).value)) 
    print()

    tree = [6,2,8,0,4,7,9,None,None,3,5]
    p = TreeNode(2)
    q = TreeNode(4)
    print("Input: tree = " + str(tree) + ", p = " + str(p.value) + ", q = " + str(q.value))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(lowest_common_ancestor_of_a_binary_search_tree(tree, p, q).value)) 
    print()

    tree = [2,1]
    p = TreeNode(2)
    q = TreeNode(1)
    print("Input: tree = " + str(tree) + ", p = " + str(p.value) + ", q = " + str(q.value))
    tree = generate_binary_tree_from_array(tree, len(tree), 0)
    print("Output: " + str(lowest_common_ancestor_of_a_binary_search_tree(tree, p, q).value)) 
    print()

main()