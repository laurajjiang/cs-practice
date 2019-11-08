#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        if j == 0:
            return -1
        while i < j:
            pivot = (i + j) // 2
            if pivot == i:
                return i if nums[i] == target else -1
            if self.in_range(nums, target, i, pivot):
                j = pivot
            elif self.in_range(nums, target, pivot, j):
                i = pivot
            else:
                return -1

    def in_range(self, nums, target, i, j):
        start, end = nums[i], nums[j - 1]
        if start == end:
            return start == target
        elif start < end:
            return start <= target and target <= end
        else:
            return start <= target or target <= end


# @lc code=end

