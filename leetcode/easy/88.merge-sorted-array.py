#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = n - 1, m - 1, m + n - 1
        while i >= 0:
            if k == -1:
                nums1[: i + 1] = nums2[: i + 1]
                return nums1
            if nums2[i] >= nums1[j]:
                nums1[k] = nums2[i]
                k -= 1
                i -= 1
                continue
            else:
                nums1[k] = nums1[j]
                k -= 1
                j -= 1

