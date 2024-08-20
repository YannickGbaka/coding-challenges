from Stack import Stack


def next_greater_element(lst):
    index = 0
    list_size = len(lst)
    output = []
    
    while index < list_size:
        found = False
        my_stack = fill_stack(lst)
        
        while not my_stack.is_empty():
            popped = my_stack.pop()
            if popped > lst[index]:
                output.append(popped)            
                found = True
                break
        if not found:
            output.append(-1)
        index += 1
    return output
        
def fill_stack(lst) -> Stack:
    stack = Stack()
    for el in lst[::-1]:
        stack.push(el)
    return stack