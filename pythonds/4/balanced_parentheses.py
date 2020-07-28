"""
Write an algorithm that will read a string of parentheses from 
left to right and decide whether the symbols are balanced.
"""

from ds_implementation import Stack


def parChecker(parString: str) -> bool:
    stack = Stack()
    idx = 0

    while idx < len(parString):
        curr = parString[idx]
        if curr == "(":
            stack.push(curr)
        else:
            if stack.isEmpty():
                return False
            if curr == ")":
                stack.pop()
        idx += 1
    return True


print(parChecker("((()))"))
print(parChecker("(()"))

