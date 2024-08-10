from Stack import Stack
from Queue import MyQueue


def reverse_k_elements(queue, k):
    if k < 0 or k > queue.size() or queue.is_empty():
        return None
    
    stack1 = Stack()
    stack2 = Stack()

    for i in range(k):
        stack1.push(queue.dequeue()) 
    
    reduced_queue_size = queue.size()
    
    for i in range(k):
        queue.enqueue(stack1.pop())
    
    for i in range(reduced_queue_size):
        stack1.push(queue.dequeue())
        stack2.push(stack1.pop())
        queue.enqueue(stack2.pop())
    
    

    # Replace this placeholder return statement with your code
    return queue


# def reverse(arr):
#     new_array = []
#     for i in range(len(arr)-1, -1, -1):
#         new_array.append(arr[i])
#     return new_array