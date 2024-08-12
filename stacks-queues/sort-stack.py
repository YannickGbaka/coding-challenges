from Stack import MyStack


def sort_stack(stack):
    temp_stack = MyStack()

    while not stack.is_empty():
        current_element = stack.pop()
        peek = None
        if not stack.is_empty():
            peek = stack.peek()
        if current_element < peek:
            pass
        else:
            temp_stack.push(current_element)
    
    # Replace this placeholder return statement with your code
    return temp_stack