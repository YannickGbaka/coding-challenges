# from Stack import Stack
from Queue import MyQueue
#Given a number n, generate a list of binary numbers from 1  n in the form of a string using a queue.

def find_bin(n):
    myQueue = MyQueue()
    for i in range(1, n):
        myQueue.enqueue(bin(i)[2:])
    return myQueue.queue_list