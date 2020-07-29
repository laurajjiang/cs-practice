"""
Implementation of basic data structures
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, val):
        self.items.append(val)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self, val):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
