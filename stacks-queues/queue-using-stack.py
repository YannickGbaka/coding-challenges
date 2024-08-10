from Stack import Stack

class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.aux_stack = Stack()
    
    def enqueue(self, data):
        self.main_stack.push(data)
    
    def dequeue(self):
        if self.aux_stack.is_empty():
            while not self.main_stack.is_empty():
                self.aux_stack.push(self.main_stack.pop())
            
        return self.aux_stack.pop()
            