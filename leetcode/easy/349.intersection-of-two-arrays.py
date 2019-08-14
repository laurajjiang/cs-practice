#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # r, set1, set2 = set(), set(nums1), set(nums2)
        # for num in set1:
        #    if num in set2:
        #        r.add(num)
        # return r

        return set(nums1).intersection(set(nums2))

