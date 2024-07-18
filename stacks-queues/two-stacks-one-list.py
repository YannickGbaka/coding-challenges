#Design a data structure TwoStacks, that represents two stacks using a single list, where both stacks share the same list for storing elements.
#The following operations must be supported:
#push1(value): Takes an integer value and inserts it into the first stack.
#push2(value): Takes an integer value and inserts it into the second stack.
#pop1(): Removes the top element from the first stack and returns it.
#pop2(): Removes the top element from the second stack and returns it.


class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.stack_lst = [0] * size
        self.top_first = -1
        self.top_second = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top_first + 1 >= self.top_second:
            raise Exception("Stack overflow")
        self.top_first += 1
        self.stack_lst[self.top_first] = value

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top_first >= self.top_second - 1:
            raise Exception("Stack overflow")
        self.top_second -= 1
        self.stack_lst[self.top_second] = value

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top_first == -1:
            raise Exception("Stack underflow")
        popped_value = self.stack_lst[self.top_first]
        self.top_first -= 1
        return popped_value

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top_second == self.size:
            raise Exception("Stack underflow")
        popped_value = self.stack_lst[self.top_second]
        self.top_second += 1
        return popped_value
