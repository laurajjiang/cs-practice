#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n != 0:
            n /= 3
        if n == 1:
            return True
        return False


# @lc code=end

