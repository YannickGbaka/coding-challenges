from Node import Node
from LinkedList import LinkedList


def reverse(head):
    current = head
    previous = None
    
    # 1 | A -> 2 | B -> 3 | C -> 4 | D -> NULL
    # 2 -> 1
    # 1 -> Null
    #first step 
    # 1->N = P 
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        
    head = previous
    return head