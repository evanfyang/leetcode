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

def reverse_alternating_k_element_sublist(head, k):
    if k <= 1 or head is None:
        return head
    
    previous_pointer = None
    current_pointer = head
    
    while current_pointer is not None:
        last_node_of_previous_part = previous_pointer
        last_node_of_sub_list = current_pointer
        next_pointer = None
        
        i = 0
        while current_pointer is not None and i < k:
            next_pointer = current_pointer.next
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer
            current_pointer = next_pointer
            i += 1
        
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous_pointer
        else:
            head = previous_pointer
        
        last_node_of_sub_list.next = current_pointer
        
        i = 0
        while current_pointer is not None and i < k:
            previous_pointer = current_pointer
            current_pointer = current_pointer.next
            i += 1
        
    return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)

    print("Nodes of original linked list are: ", end='')
    head.print_list()
    result = reverse_alternating_k_element_sublist(head, 2)
    print("Nodes of reversed linked list are: ", end='')
    result.print_list()

main()
    
