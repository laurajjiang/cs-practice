#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XORing solution
        a = 0
        for item in nums:
            a ^= item
        return a

        # hash table solution
        hash = {}
        for item in nums:
            try:
                hash.pop(item)
            except:
                hash[item] = 1
        return hash.popitem()[0]
