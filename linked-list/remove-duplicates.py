from LinkedList import LinkedList
from Node import Node

#Given the head of a singly linked list, remove any duplicate nodes from the list in place,
# ensuring that only one occurrence of each value is retained in the modified list.

#the space complexity of this algo is O(n)
#the time complexity is O(n)
# we could use a double while loop for a O(n^2) as time complexity and a O(1) as space complexity 

def remove_duplicates(head):
    current = head
    unique_sets = set()
    previous = None
    
    while current:
        n = current.next
        if current.data in unique_sets:
            previous.next = n
            current = previous
        else:
            unique_sets.add(current.data)
        previous = current
        current = n
    return head

