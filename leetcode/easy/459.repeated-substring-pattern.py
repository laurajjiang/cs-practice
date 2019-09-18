#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for k in range(1, len(s) // 2 + 1):
            if s == s[k:] + s[:k]:
                return True
        return False

