# Definition for singly-linked list.
class Node:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
    
    def print_list(self):
        node = self
        while node is not None:
            print(node.value, end="->")
            node = node.next
        print("None", end="")

def reverse_linked_list_ii(head, left, right):
    if left == right:
        return head

    current_pointer, previous_pointer = head, None

    i = 0
    while current_pointer is not None and i < left - 1:
        previous_pointer = current_pointer
        current_pointer = current_pointer.next
        i += 1

    last_node_of_first_part = previous_pointer
    last_node_of_sublist = current_pointer
    next_pointer = None

    i = 0
    while current_pointer is not None and i < right - left + 1:
        next_pointer = current_pointer.next
        current_pointer.next = previous_pointer
        previous_pointer = current_pointer
        current_pointer = next_pointer
        i += 1


    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous_pointer
    else:
        head = previous_pointer

    last_node_of_sublist.next = current_pointer

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_linked_list_ii(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
