from LinkedList import LinkedList
from Node import Node

#challenge : Given the head of a linked list and a target, value
#return the updated linked list head after adding the target value at the end of the linked list.

def delete_at_tail(head, target):
    if head is None:
        head = Node(target)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = Node(target)
    return head