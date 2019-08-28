#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in reversed(range(len(arr))):
            if arr[i] == 0:
                arr.insert(i, 0)
                del arr[-1]

