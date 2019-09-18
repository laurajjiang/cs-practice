#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
        return True

