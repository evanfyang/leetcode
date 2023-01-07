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
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternating_k_element_sublist(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
    
