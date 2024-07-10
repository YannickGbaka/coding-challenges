#Given the head of a linked list, check whether or not a cycle is present in the linked list.
# A cycle is present in a linked list if at least one node can be reached again by traversing the next pointer. 
# If a cycle exists, return TRUE; otherwise, return FALSE.

from LinkedList import LinkedList
from Node import Node

def detect_cycle(head):
    current = head
    adresses = set()
    
    while current:
        if current.next in adresses:
            return True
        adresses.add(current)
        current = current.next
    return False


def detect_cycle2(head):
    p1 = head
    p2 = head
    
    while p1 and p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        
        if p1 == p2:
            return True
        
    return False    
    