# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = value
        self.next = next

def middle_of_the_linked_list(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        
    return slow_pointer

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Middle Node: " + str(middle_of_linked_list(head).value))

    head.next.next.next.next.next = ListNode(6)
    print("Middle Node: " + str(middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = ListNode(7)
    print("Middle Node: " + str(middle_of_linked_list(head).value))
    
main()
