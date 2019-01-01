"""
    This problem was asked by Apple.

    Implement a queue using two stacks. Recall that a queue is
    a FIFO (first-in, first-out) data structure with the following
    methods: enqueue, which inserts an element into the queue, and
    dequeue, which removes it.
"""

class Stack:

    def __init__(self):
        self._top = -1
        self._vals = []

    def push(self, val):
        self._vals.append(val)
        self._top += 1

    def pop(self):
        if self._top == -1:
            return None
        ret = self._vals[self._top]
        del self._vals[self._top]
        self._top -= 1
        return ret


class Queue:
    def __init__(self):
        self._queue = Stack()
        self._temp = Stack()

    def enqueue(self, val):
        self._queue.push(val)

    def dequeue(self):
        while (val = self._queue.pop()) is not None:
            self._temp.push(val)

        ret = self._temp.pop()

        while (val = self._temp.pop()) is not None:
            self._queue.push(val)

        return ret
