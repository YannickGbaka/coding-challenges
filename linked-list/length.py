from LinkedList import LinkedList
from Node import Node

def length(head):
    if head == None:
        return 0
    
    current = head
    count = 0
    while current:
        count +=1
        current = current.next
        
    return count
        