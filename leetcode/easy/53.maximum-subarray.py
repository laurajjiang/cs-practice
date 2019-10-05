#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = [0] * len(nums)
        maxSum[0] = nums[0]
        for i in range(1, len(nums)):
            maxSum[i] = max(maxSum[i - 1] + nums[i], nums[i])
        return max(maxSum)


# @lc code=end

