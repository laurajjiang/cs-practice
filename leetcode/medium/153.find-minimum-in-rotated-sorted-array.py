#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[-1]
        mid = n // 2
        if nums[0] < nums[mid]:
            if nums[-1] >= nums[mid]:
                return self.findMin(nums[:mid])
            return self.findMin(nums[mid + 1 :])
        else:
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            return self.findMin(nums[:mid])


# @lc code=end

