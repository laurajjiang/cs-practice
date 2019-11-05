#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        if len(typed) < len(name):
            return False
        if typed == name:
            return True

        while i < len(name) - 1:
            if name[i] == typed[i]:
                i += 1
                j += 1
            else:
                j += 1
            if j == len(typed) and i != len(name):
                return False
        return True


# @lc code=end

