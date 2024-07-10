class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    @staticmethod
    def size(head) -> int:
        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        return length