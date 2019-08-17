#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # adapted solution from 217
        map = {}
        for i, j in enumerate(nums):
            if j in map and (i - map[j]) <= k:
                return True
            map[j] = i
        return False

