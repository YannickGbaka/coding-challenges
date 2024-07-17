from LinkedList import LinkedList
from Node import Node

#Given the heads of two linked lists, head1 and head2, as inputs. Implement the union and intersection functions for the linked lists. The order of elements in the output lists doesn’t matter.
#Here’s how you will implement the functions:
#Union: This function will take two linked lists as input and return a new linked list containing all the unique elements.


def union(head1, head2):
    tail1 = None
    current1 = head1
    current2 = head2
    while current1:
        previous = None
        while current2:
            next_element = current2.next
            if current1.data == current2.data:
                previous.next = current2.next
                current2 = None
            else:
                previous = current2
            current2 = next_element
        if current1.next is None:
            tail1 = current1
        current1 = current1.next
    tail1.next = head2
    # Replace this placeholder return statement with your code
    return head1