from Node import Node
from LinkedList import LinkedList

def delete(head, value):
    if head is None:
        return False
    
    if head.next is None:
        if head.data == value:
            return True
        return False
    else:
        current = head
        previous = current
        while current:
            if current.data == value:
                previous.next = current.next
                current = None
                return True
            current = current.next
        return False