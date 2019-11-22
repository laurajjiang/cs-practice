#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start

import math


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)):
            return -1
        base = math.ceil(len(B) / len(A))

        for i in range(3):
            if B in A * (base + i):
                return base + i
        return -1


# @lc code=end

