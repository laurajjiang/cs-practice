#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # interesting solution using a stack, but times out ):
        stack = []
        while nums:
            temp = nums.pop()
            while stack and temp < stack[-1]:
                nums.append(stack.pop())
            stack.append(temp)
        return stack

