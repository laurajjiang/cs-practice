#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for center in range(len(nums) - 1):
            left = 0
            right = len(nums) - 1

            while left < center and center < right:
                temp = nums[left] + nums[center] + nums[right]

                if temp == 0:
                    if (nums[left], nums[center], nums[right]) not in res:
                        res.add((nums[left], nums[center], nums[right]))
                        left += 1
                        right -= 1
                    elif temp > 0:
                        right -= 1
                    elif temp < 0:
                        left += 1

        return list(res)


# @lc code=end

