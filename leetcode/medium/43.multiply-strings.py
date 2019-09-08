#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for c in num1:
            n1 = n1 * 10 + (ord(c) - ord("0"))
        for c in num2:
            n2 = n2 * 10 + (ord(c) - ord("0"))
        return str(n1 * n2)

