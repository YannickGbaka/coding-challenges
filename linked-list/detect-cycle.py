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

