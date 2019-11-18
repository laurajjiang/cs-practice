#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)
        for char in t:
            if len(stack) > 0 and char == stack[0]:
                stack.pop(0)
        return len(stack) == 0


# @lc code=end

