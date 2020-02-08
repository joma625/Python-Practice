# data structure: 1. Queue: FIFO 2. Stack: FILO
from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.popleft()


mystack = Stack()
mystack.push('a')
print(mystack.stack)

myqueue = Queue()
myqueue.enqueue('a')
myqueue.dequeue()
print(myqueue.queue)
