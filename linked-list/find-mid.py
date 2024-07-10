from LinkedList import LinkedList
from Node import Node
import math

#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node. This happens when the length of the list is even, and the second
#middle node occurs at length / 2. Otherwise, if the length of the list is odd, the middle node occurs at (length / 2) + 1

def find_mid(head):
    
   length = LinkedList.size(head)
   
   if length == 1:
       return head.data
   
   current = head
   half_length = math.ceil(length // 2)
   for i in range(half_length):
       current = current.next
   
   return current.data
        
    

