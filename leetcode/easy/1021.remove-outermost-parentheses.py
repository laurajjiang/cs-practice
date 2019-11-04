#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        count = 0
        first = 0
        for i in range(len(S)):
            if S[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 0:
                res += S[first + 1 : i]
                first = i + 1
        return res


# @lc code=end

