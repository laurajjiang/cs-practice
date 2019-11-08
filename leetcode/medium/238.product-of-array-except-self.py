#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = [1 for _ in range(len(nums))]
        lo, hi = 0, len(nums) - 1
        left_prod, right_prod = 1, 1

        while lo < len(nums):
            res[lo] *= left_prod
            res[hi] *= right_prod
            left_prod *= nums[lo]
            right_prod *= nums[hi]
            lo += 1
            hi -= 1
        return res


# @lc code=end

