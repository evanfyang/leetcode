# Definition for singly-linked list.
class ListNode:
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
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print("Linked list has cycle: " + str(linked_list_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("Linked list has cycle: " + str(linked_list_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Linked list has cycle: " + str(linked_list_cycle(head)))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next
    print("Linked list cycle length: " + str(linked_list_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Linked list cycle length: " + str(linked_list_cycle_length(head)))

main()
