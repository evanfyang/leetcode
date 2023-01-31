from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value
    
    def __str__(self):
        string = "["
        traverse = self

        while traverse is not None:
            string += str(traverse.value)
            if traverse.next is not None:
                string += ", "
            else:
                string += "]"
            traverse = traverse.next
        
        return string

def linked_list(array=list()):
    if len(array) == 0:
        return None
    head = tail = ListNode(array[0], None)
    for index in range(1, len(array)):
        node = ListNode(array[index], None)
        tail.next = node
        tail = tail.next
    return head

def merge_k_sorted_lists_leetcode(lists):
    min_heap = list()

    for index in range(len(lists)):
        root = lists[index]
        if root is not None:
            heappush(min_heap, (root.value, index))

    merged_list_head, merged_list_tail = None, None
    while min_heap:
        value, index = heappop(min_heap)
        if merged_list_head is None:
            merged_list_head = merged_list_tail = ListNode(value)
        else:
            merged_list_tail.next = ListNode(value)
            merged_list_tail = merged_list_tail.next
        
        if lists[index].next is not None:
            lists[index] = lists[index].next
            heappush(min_heap, (lists[index].value, index))
    
    return merged_list_head

def merge_k_sorted_lists(lists):
    min_heap = []

    # put the root of each list in the min heap
    for root in lists:
        if root is not None:
            heappush(min_heap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    merged_list_head, merged_list_tail = None, None
    while min_heap:
        node = heappop(min_heap)
        if merged_list_head is None:
            merged_list_head = merged_list_tail = node
        else:
            merged_list_tail.next = node
            merged_list_tail = merged_list_tail.next

        if node.next is not None:
            heappush(min_heap, node.next)

    return merged_list_head
    
def main():
    lists = [[2,6,8],[3,6,7],[1,3,4]]
    print("Input: lists = " + str(lists))
    lists = [linked_list(array) for array in lists]
    print("Output: " + str((merge_k_sorted_lists_leetcode(lists))))
    print()

    lists = [[5,8,9],[1,7]]
    print("Input: lists = " + str(lists))
    lists = [linked_list(array) for array in lists]
    print("Output: " + str((merge_k_sorted_lists_leetcode(lists))))
    print()

    lists = [[1,4,5],[1,3,4],[2,6]]
    print("Input: lists = " + str(lists))
    lists = [linked_list(array) for array in lists]
    print("Output: " + str((merge_k_sorted_lists_leetcode(lists))))
    print()

    lists = []
    print("Input: lists = " + str(lists))
    lists = [linked_list(array) for array in lists]
    print("Output: " + str((merge_k_sorted_lists_leetcode(lists))))
    print()

    lists = [[]]
    print("Input: lists = " + str(lists))
    lists = [linked_list(array) for array in lists]
    print("Output: " + str((merge_k_sorted_lists_leetcode(lists))))
    print()

main()