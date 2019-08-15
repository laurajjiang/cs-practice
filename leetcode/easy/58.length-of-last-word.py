#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.strip():
            last = s.split()[-1]
            return len(last)
        else:
            return 0

