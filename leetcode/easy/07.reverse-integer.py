#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x):
        temp = int(str(abs(x))[::-1])
        if temp > 2147483647 or temp < -2147483647:  # max limit (-2^31 to 2^31 -1)
            return 0
        if x > 0:
            return temp
        else:
            return -temp

