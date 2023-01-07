# Definition for singly-linked list.
class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def palindrome_linked_list(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next 
        slow_pointer = slow_pointer.next

    head_second_half_reversed = reverse(slow_pointer)
    copy_head_second_half_reversed = head_second_half_reversed
    head_first_half = head
    
    while head_first_half is not None and head_second_half_reversed is not None:
        if head_first_half.value != head_second_half_reversed.value:
            return False
        head_first_half = head_first_half.next
        head_second_half_reversed = head_second_half_reversed.next

    self.reverse(copy_head_second_half_reversed)
    
    if head_first_half is None or head_second_half_reversed is None:
        return True

def reverse(head):
    previous_node = None

    while head is not None:
        next_node = head.next
        head.next = previous_node
        previous_node = head
        head = next_node

    return previous_node

def main():
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(2)
    print("Is palindrome: " + str(palindrome_linked_list(head)))

    head.next.next.next.next.next = ListNode(2)
    print("Is palindrome: " + str(palindrome_linked_list(head)))
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print("Is palindrome: " + str(palindrome_linked_list(head)))

    head = ListNode(1)
    head.next = ListNode(2)
    print("Is palindrome: " + str(palindrome_linked_list(head)))
    
main()
