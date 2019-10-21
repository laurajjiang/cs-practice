#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        p1 = 1
        p2 = 1 if s[0] != 0 else 0

        for i in range(2, len(s) + 1):
            sum = 0
            if s[i - 1] != "0":
                sum += p2
            if s[i - 2] != "0" and s[i - 2 : i] <= 26:
                sum += p1
                p1 = p2
            else:
                p1 = p2
        return p2


# @lc code=end

