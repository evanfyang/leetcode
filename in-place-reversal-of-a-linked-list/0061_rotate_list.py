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
    
def rotate_list(head, k):
    if head is None or head.next is None or k <= 0:
        return head

    last_node = head
    linked_list_length = 1

    while last_node.next is not None:
        last_node = last_node.next
        linked_list_length += 1 

    last_node.next = head
    k %= linked_list_length
    skip_length = linked_list_length - k
    last_node_of_rotated_list = head

    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate_list(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()

main()
