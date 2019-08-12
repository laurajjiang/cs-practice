#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.upper(), word.lower(), word.title()]

