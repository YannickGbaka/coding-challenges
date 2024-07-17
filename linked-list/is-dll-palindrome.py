# Given the head of a doubly linked list, check whether the doubly linked list is a palindrome or not.
# Return TRUE if it is a palindrome; otherwise, return FALSE.
# A palindrome is any string or sequence that reads the same from both ends. For example, 2002 is a palindrome.


def is_palindrome(head) -> bool:
    
    current_from_head = head
    tail = get_tail(head)
    
    while tail and current_from_head != tail:
        if tail.data != current_from_head.data :
            return False
        tail = tail.prev
        current_from_head = current_from_head.next
    return True
        

def get_tail(head):
    current = head
    while current.next:
        current = current.next
    return current