#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        min_prod = max_prod = curr_max = nums[0]
        for i in range(1, len(nums)):
            a, b, c = nums[i], min_prod * nums[i], max_prod * nums[i]
            # print("curr: ", nums[i])
            # print("min: ", min_prod)
            # print("max: ", max_prod)
            min_prod = min(a, b, c)
            max_prod = max(a, b, c)
            curr_max = max(max_prod, curr_max)
            # print("min after: ", min_prod)
            # print("curr max: ", curr_max)
        return curr_max


# @lc code=end

