#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums)
        nums.sort()
        max = 0
        i = 0
        while i < len(nums):
            max = max + min(nums[i], nums[i] + 1)
            i += 2
        return max


# @lc code=end

