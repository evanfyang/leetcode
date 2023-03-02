# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        value = value
        left = left
        right = right

def generate_binary_tree_from_array(array, array_length, array_index):
    root = None
    # Base case for recursion 
    if array_index < array_length:
        if array[array_index] is None:
            return root
        root = TreeNode(array[array_index]) 
        # insert left child 
        root.left = generate_binary_tree_from_array(array, array_length, 2 * array_index + 1)
        # insert right child 
        root.right = generate_binary_tree_from_array(array, array_length, 2 * array_index + 2)
          
    return root

def subtree_of_another_tree(root, sub_root):        
    if not sub_root:
        return True
    if not root:
        return False

    if same_tree(root, sub_root):
        return True
    
    return subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)

def same_tree(p, q):
    if p is None and q is None:
        return True
    if not p or not q or p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

def main():
    root = [3,4,5,1,2]
    sub_root = [4,1,2]
    print("Input: root = " + str(root) + " sub_root = " + str(sub_root))
    print("Output: " + str(subtree_of_another_tree(root, sub_root)))
    print()

    root = [3,4,5,1,2,None,None,None,None,0]
    sub_root = [4,1,2]
    print("Input: root = " + str(root) + " sub_root = " + str(sub_root))
    print("Output: " + str(subtree_of_another_tree(root, sub_root)))
    print()

main()