# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def start_of_linked_list_cycle(head):
    slow_pointer = head
    fast_pointer = head
    cycle_exists = False

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            cycle_exists = True
            break

    if not cycle_exists:
        return None

    cycle_length = 1
    slow_pointer = slow_pointer.next

    while slow_pointer is not None:
        slow_pointer = slow_pointer.next
        cycle_length += 1
        if slow_pointer == fast_pointer:
            break

    slow_pointer = head
    for i in range(cycle_length):
        if fast_pointer is not None:
            fast_pointer.next

    while slow_pointer != fast_pointer:
        if slow_pointer is not None:
            slow_pointer = slow_pointer.next
        if fast_pointer is not None:
            fast_pointer = fast_pointer.next

    return slow_pointer

def main():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  head.next.next.next.next.next = ListNode(6)

  head.next.next.next.next.next.next = head.next.next
  print("Linked list cycle start: " + str(start_of_linked_list_cycle(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("Linked list cycle start: " + str(start_of_linked_list_cycle(head).value))

  head.next.next.next.next.next.next = head
  print("Linked list cycle start: " + str(start_of_linked_list_cycle(head).value))
    
main()
