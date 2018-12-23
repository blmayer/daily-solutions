"""
    This problem was asked by Amazon.

    Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
    Each method should run in constant time.
"""

class Stack:

    def __init__(self):
        self._top = -1
        self._max = []
        self._vals = []

    def max(self):
        if self._top == -1:
            return None

        return self._max[self._top]

    def push(self, val):
        self._vals.append(val)

        if self.max() is None or val > self.max():
            self._max.append(val)
        else:
            self._max.append(self.max())

        self._top += 1


    def pop(self):
        if self._top == -1:
            return None

        del self._max[self._top]
        ret = self._vals[self._top]
        del self._vals[self._top]
        self._top -= 1

        return ret

