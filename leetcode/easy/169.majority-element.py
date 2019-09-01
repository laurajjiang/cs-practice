#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = list(nums)
        l.sort()
        return l[len(l) // 2]

