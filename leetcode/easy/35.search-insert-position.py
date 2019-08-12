#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # simple but slow method
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)

        # binary search

        beg = 0
        mid = len(nums) // 2
        end = len(nums) - 1

        while beg + 1 != end and beg != end:
            if target == nums[mid]:
                return mid
            if target <= nums[mid]:
                end = mid
                mid = (beg + end) // 2
            elif target > nums[mid]:
                beg = mid
                mid = (beg + end) // 2

        if target > nums[end]:
            return end + 1
        if target <= nums[beg]:
            return 0
        return end
