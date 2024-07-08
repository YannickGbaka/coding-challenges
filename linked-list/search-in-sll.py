from LinkedList import LinkedList
from Node import Node

#challenge : Given the head of a linked list and a target, value
#return the updated linked list head after adding the target value at the end of the linked list.

def search(head, value) -> bool:
    if head is None:
        return False
    
    current = head
    if current.next is None and current.data != value:
        return False
    elif current.next is None and current.data == value:
        return True
    else:
        while current.next:
            if current.data == value:
                return True
            current = current.next
        return False
    