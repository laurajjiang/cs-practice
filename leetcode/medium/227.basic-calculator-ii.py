#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start

import re


class Solution:
    def calculate(self, s: str) -> int:
        exp_split = re.split("(\W)", s)
        values, operators = [], []
        for char in exp_split:
            if char != " " and char != "":
                if not self.isOperator(char):
                    values.append(char)
                else:
                    while len(operators) > 0 and self.checkPrecedence(
                        operators[-1]
                    ) >= self.checkPrecedence(char):
                        curr_op = operators.pop()
                        val_b = values.pop()
                        val_a = values.pop()
                        values.append(
                            self.performOperations(curr_op, int(val_a), int(val_b))
                        )
                    operators.append(char)
        while len(operators) > 0:
            curr_op = operators.pop()
            val_b = values.pop()
            val_a = values.pop()
            values.append(self.performOperations(curr_op, int(val_a), int(val_b)))
        return values[-1]

    def isOperator(self, char):
        if char == "+" or char == "-" or char == "/" or char == "*":
            return True
        return False

    def checkPrecedence(self, op):
        if op == "/" or op == "*":
            return 1
        return 0

    def performOperations(self, op, a, b):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return int(a / b)


# @lc code=end

