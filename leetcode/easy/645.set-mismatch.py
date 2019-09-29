#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n * (n + 1) // 2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]

