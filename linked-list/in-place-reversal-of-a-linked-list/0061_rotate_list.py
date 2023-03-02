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
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    print("Nodes of original linked list are: ", end='')
    head.print_list()
    result = rotate_list(head, 3)
    print("Nodes of rotated linked list are: ", end='')
    result.print_list()

main()
