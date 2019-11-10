#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0

        d = collections.Counter()
        max_freq = 0

        while right < len(s):
            d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])
            while right - left + 1 - max_freq > k:
                d[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


# @lc code=end

