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

def convert_sorted_array_to_binary_search_tree(nums):
    def generate_binary_search_tree(left, right):
        if left > right:
            return None
        
        middle = (left + right) // 2
        
        root = TreeNode(nums[middle])
        root.left = generate_binary_search_tree(left, middle - 1)
        root.right = generate_binary_search_tree(middle + 1, right)

        return root

    return generate_binary_search_tree(0, len(nums) - 1)

def main():
    nums = [-10,-3,0,5,9]
    print("Input: nums = " + str(nums))
    print("Output: " + str(convert_sorted_array_to_binary_search_tree(nums).level_order_traversal()))
    print()

    nums = [1,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(convert_sorted_array_to_binary_search_tree(nums).level_order_traversal()))
    print()

main()        