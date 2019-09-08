#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        output = []
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                i = mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                output.append(i + 1)
                i = mid
                while i < len(nums) and nums[i] == target:
                    i += 1
                output.append(i - 1)
                return output
            if target < nums[mid]:
                high = mid - 1
            if target > nums[mid]:
                low = mid + 1
        return [-1, -1]

