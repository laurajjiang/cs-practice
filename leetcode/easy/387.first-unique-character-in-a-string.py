#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        if len(s) == 1:
            return 0

        idx = len(s)
        for i in set(s):
            if s.count(i) == 1:
                idx = min(idx, s.index(i))
        return idx if idx != len(s) else -1


# @lc code=end

