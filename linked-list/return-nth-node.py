from LinkedList import LinkedList
from Node import Node

#Try to solve the Return the Nth Node from End problem.
#Given the head of a linked list, return the 𝑛𝑡ℎ node from the end of the linked list.


def find_nth(head, n) -> Node:    
    target = size(head) - n

    if target == 0:
        return head
    
    if target > 0:
        target +=1

    current = head
    k = 1
    
    while k != target:
        current = current.next
        k +=1
    return current

def size(head) -> int:
    length = 0
    current = head
    while current:
        length +=1
        current = current.next
    return length
        
