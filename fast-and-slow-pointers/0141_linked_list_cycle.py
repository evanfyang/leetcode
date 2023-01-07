# Definition for singly-linked list.
class Node:
    def __init__(self, x):
         self.val = x
         self.next = None
    
def linked_list_cycle(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if slow_pointer == fast_pointer:
            return True

    return False

def linked_list_cycle_length(head):
    slow_pointer = head
    fast_pointer = head
    
    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if slow_pointer == fast_pointer:
            break
    
    cycle_length = 1
    fast_pointer = fast_pointer.next
    
    while fast_pointer is not slow_pointer:
        cycle_length += 1
        fast_pointer = fast_pointer.next
    
    return cycle_length
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(linked_list_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(linked_list_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(linked_list_cycle(head)))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(linked_list_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(linked_list_cycle_length(head)))

main()
