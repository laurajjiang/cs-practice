#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        value = self.myPow(x, n // 2)
        if n % 2 == 0:
            return value * value
        else:
            return value * value * x

