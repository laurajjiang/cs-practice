#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        if num == 0:
            return "0"
        if num < 0:
            result += "-"
        num = abs(num)
        rem = []
        while num > 0:
            k = int(num % 7)
            rem.append(str(k))
            num = (num - k) / 7

        rem.reverse()
        for i in rem:
            result += i
        return result

