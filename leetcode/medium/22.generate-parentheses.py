#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, n, n)
        return res

    def helper(self, res, open, close, curr=""):
        if open == 0 and close == 0:
            res.append(curr)

        if open < 0 or close < 0:
            return

        if open == close:
            self.helper(res, open - 1, close, curr + "(")

        if open < close:
            self.helper(res, open - 1, close, curr + "(")
            self.helper(res, open, close - 1, curr + ")")


# @lc code=end

