from Stack import Stack

class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.aux_stack = Stack()
    
    def enqueue(self, value):
        if self.main_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.aux_stack.push(self.main_stack.pop())
            
            self.main_stack.push(value)

            while not self.aux_stack.is_empty():
               self.main_stack.push(self.aux_stack.pop())


    # Removes the element from the queue
    def dequeue(self):
        if not self.main_stack.is_empty():
            return self.main_stack.pop()
            