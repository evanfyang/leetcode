# Definition for singly-linked list.
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def reorder_list(head):
    if head is None and head.next is None: 
        return 

    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    head_second_half = self.reverse(slow_pointer)
    head_first_half = head

    while head_first_half is not None and head_second_half is not None:
        first_half_next_node = head_first_half.next
        head_first_half.next = head_second_half 
        head_first_half = first_half_next_node

        second_half_next_node = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = second_half_next_node

    if head_first_half is not None:
        head_first_half.next = None

def reverse(self, head):
    previous_node = None
    while head is not None:
        next_node = head.next
        head.next = previous_node
        previous_node = head
        head = next_node
    return previous_node

def main():
    
    print("Input: " + head.print_list())
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    print("Output: " + head.print_list())

main()
