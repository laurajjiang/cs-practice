#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map:
                return True
            map[i] = True
        return False

