#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) ** 2 == num

