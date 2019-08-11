#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits):
        length = len(digits) - 1
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        if digits[length] != 9:
            digits[length] += 1
            return digits
        for i in range(len(digits)):
            # not sure why keeping this loop increases runtime?
            if digits[-1] == 9:
                digits[-1] = 0
                digits[:-1] = self.plusOne(digits[:-1])
                return digits
