#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums, target):
        # found an interesting hash table solution
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                return [map[num], i]
            map[target - num] = i

