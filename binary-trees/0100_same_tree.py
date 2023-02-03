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
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
          
    return root

def same_tree(p, q):
    if not p and not q:
        return True
    
    if not p or not q or p.value != q.value:
        return False
    
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

def main():
    p = [10,4,15,1,None,14]
    q = [10,4,15,1,None,14]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

    p = [10,4,15,1,None,14]
    q = [10,4,15,1,None,14,20]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

    p = [10,9,15,1,None,14,20]
    q = [10,4,15,1,None,14,20]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

    p = [1,2,3]
    q = [1,2,3]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

    p = [1,2]
    q = [1,None,2]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

    p = [1,2,1]
    q = [1,1,2]
    print("Input: p = " + str(p) + ", q = " + str(q))
    p = generate_binary_tree_from_array(p, len(p), 0)
    q = generate_binary_tree_from_array(q, len(q), 0)
    print("Output: " + str(same_tree(p, q)))
    print()

main()