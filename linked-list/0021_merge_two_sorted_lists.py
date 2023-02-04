# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def generate_linked_list_from_array(array):
    head = tail = ListNode()
    for element in array:
        tail.next = ListNode(element)
        tail = tail.next
    return head.next

def generate_array_from_linked_list(linked_list):
    array = list()
    while linked_list:
        array.append(linked_list.value)
        linked_list = linked_list.next
    return array

def merge_two_sorted_lists(list1, list2):
    head = tail = ListNode() 

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1        
    elif list2:
        tail.next = list2

    return head.next

def main():
    list1 = [1,2,4]
    list2 = [1,3,4]
    print("Input: list1 = " + str(list1) + ", list2 = " + str(list2))
    list1 = generate_linked_list_from_array(list1)
    list2 = generate_linked_list_from_array(list2)
    merged_list = generate_array_from_linked_list(merge_two_sorted_lists(list1, list2))
    print("Output: " + str(merged_list)) 
    print() 

    list1 = []
    list2 = []
    print("Input: list1 = " + str(list1) + ", list2 = " + str(list2))
    list1 = generate_linked_list_from_array(list1)
    list2 = generate_linked_list_from_array(list2)
    merged_list = generate_array_from_linked_list(merge_two_sorted_lists(list1, list2))
    print("Output: " + str(merged_list)) 
    print() 

    list1 = []
    list2 = [0]
    print("Input: list1 = " + str(list1) + ", list2 = " + str(list2))
    list1 = generate_linked_list_from_array(list1)
    list2 = generate_linked_list_from_array(list2)
    merged_list = generate_array_from_linked_list(merge_two_sorted_lists(list1, list2))
    print("Output: " + str(merged_list)) 
    print() 

main()