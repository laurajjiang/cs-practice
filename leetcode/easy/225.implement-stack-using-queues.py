#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

import collections


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(self.size):
            self.queue.append(self.queue.popleft())
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.size -= 1
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
