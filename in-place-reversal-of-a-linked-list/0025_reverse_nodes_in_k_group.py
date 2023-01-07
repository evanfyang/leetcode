# Definition for singly-linked list.
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        node = self
        while node is not None:
            print(node.value, end="->")
            node = node.next
        print("None")
        print()

def reverse_nodes_in_k_group(head, k):
    if k <= 1 or head is None:
        return head

    current_pointer = head
    previous_pointer = None

    while True:
        ##### comment this block out to reverse groups in list that are not of size k #####
        ##### ----------------------------------------------------------------------- #####
        count, kth_node = 0, current_pointer
        while kth_node is not None and count < k:
            kth_node = kth_node.next
            count += 1
        if count < k: 
            return head
        ##### ----------------------------------------------------------------------- #####

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

        if current_pointer is None:
            break
        previous_pointer = last_node_of_sub_list

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
    result = reverse_nodes_in_k_group(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
 
main()
