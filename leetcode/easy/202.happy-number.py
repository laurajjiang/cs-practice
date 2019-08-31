#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            nn = str(n)
            num = sum([int(x) ** 2 for x in nn])
        if num in d:
            return False
        else:
            d[num] = 1
            if num == 1:
                return True
            n = num

