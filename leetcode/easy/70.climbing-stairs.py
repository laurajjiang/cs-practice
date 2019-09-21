#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        fib, count = [1, 2], 2
        while count < n:
            fib.append(fib[count - 1] + fib[count - 2])
            count += 1
        return fib[n - 1]

