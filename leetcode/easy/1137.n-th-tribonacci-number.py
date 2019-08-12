#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        # come back to this and draw it out to understand it better
        for i in range(n):
            a, b, c = b, c, a + b + c
        return a
