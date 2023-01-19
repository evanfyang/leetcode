# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def unique_binary_search_trees_memoized(n, map=dict()):
    if n in map:
        return map[n]
    
    if n <= 1:
        return 1
    
    count = 0

    for i in range(1, n + 1):
        count_left_subtrees = unique_binary_search_trees_memoized(i - 1, map)
        count_right_subtrees = unique_binary_search_trees_memoized(n - i, map)
        count += (count_left_subtrees * count_right_subtrees)
    
    map[n] = count
    return count

def unique_binary_search_trees_grokking(n):
    if n <= 1:
        return 1
    
    count = 0
    
    for i in range(1, n + 1):
        count_left_subtrees = unique_binary_search_trees_grokking(i - 1)
        count_right_subtrees = unique_binary_search_trees_grokking(n - i)
        count += (count_left_subtrees * count_right_subtrees)
    
    return count

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

def unique_binary_search_trees(n):
    return (factorial(2 * n) // (factorial(n + 1) * factorial(n)))

def main():
    n = 0
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

    n = 1
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

    n = 2
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

    n = 3
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

    n = 4
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

    n = 5
    print("Input: n = " + str(n))
    print("Output: " + str(unique_binary_search_trees(n)))
    print()

main()