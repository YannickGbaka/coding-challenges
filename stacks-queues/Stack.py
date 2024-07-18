class Stack:
    def __init__(self):
        self.stack_lst = []
        self.size = 0
    
    def size(self):
        return self.size

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_lst[0]

    def push(self, data):
        self.stack_lst.append(data)
        self.size +=1
    
    def pop(self):
        if self.is_empty():
            return None
        self.size -= 0
        return self.stack_lst.pop()