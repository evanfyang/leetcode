# Definition for singly-linked list.
class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_the_linked_list(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        
    return slow_pointer

def main():
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)

    print("Middle Node: " + str(middle_of_linked_list(head).value))

    head.next.next.next.next.next = node(6)
    print("Middle Node: " + str(middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = node(7)
    print("Middle Node: " + str(middle_of_linked_list(head).value))
    
main()
