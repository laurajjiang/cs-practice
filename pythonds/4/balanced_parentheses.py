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


def bracketChecker(parString: str) -> bool:
    stack = Stack()
    idx = 0

    while idx < len(parString):
        curr = parString[idx]
        if curr in "{[(":
            stack.push(curr)
        else:
            if stack.isEmpty():
                return False
            top = stack.pop()
            if not isMatch(top, curr):
                return False
        idx += 1
    return True


def isMatch(open: chr, close: chr) -> bool:
    openBrackets = "({["
    closeBrackets = ")}]"
    return openBrackets.index(open) == closeBrackets.index(close)


print(parChecker("((()))"))
print(parChecker("(()"))

print(bracketChecker("{({([][])}())}"))
print(bracketChecker("[{()]"))
