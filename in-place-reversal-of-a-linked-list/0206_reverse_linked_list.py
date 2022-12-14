# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        node = self
        while node is not None:
            print(node.value, end="->")
            node = node.next
        print("None", end="")

def reverse_linked_list(head):
    previous_pointer = None
    next_pointer = None

    while head is not None:
        next_pointer = head.next
        head.next = previous_pointer
        previous_pointer = head
        head = next_pointer

    return previous_pointer

def main():
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)

    print("Nodes of original linked list are: ", end='')
    head.print_list()
    result = reverse_linked_list(head)
    print("Nodes of reversed linked list are: ", end='')
    result.print_list()
    
main()
