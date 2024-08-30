from Stack import Stack

"""
    Design a stack data structure to retrieve the minimum value in 
    O(1)
    O(1)
    time. The following functions must be implemented:

    min(): Returns the minimum value in the stack in constant time.
    push(int value): Pushes a value onto the stack.
    pop(): Removes and returns a value from the top of the stack.
    All functions should be implemented with a time complexity of 
    
    O(1)
    O(1)
"""


class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.size = 0
        self.main_stack = []
        self.min_stack = []

    # Remove and returns value from the stack
    def pop(self):
        if self.main_stack:
          popped = self.main_stack.pop()
          if popped == self.min_stack[-1]:
            self.min_stack.pop()
          return popped
        return None

    # Pushes values into the stack
    def push(self, value):
       self.main_stack.append(value)
       if not self.min_stack or value <= self.min_stack[-1]:
         self.min_stack.append(value)
        
    # Returns minimum value from stack
    def min(self):
      if not self.min_stack:
        return None
      return self.min_stack[-1]