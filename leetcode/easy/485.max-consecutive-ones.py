#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        top = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > top:
                    top = count
            else:
                count = 0
        return top


# @lc code=end

