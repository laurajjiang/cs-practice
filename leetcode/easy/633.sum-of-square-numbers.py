#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))
        i, j = 0, n
        while i <= j:
            res = i * i + j * j
            if res == c:
                return True
            elif res > c:
                j -= 1
            else:
                i += 1
        return False

