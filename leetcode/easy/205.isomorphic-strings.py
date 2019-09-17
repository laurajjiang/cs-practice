#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t == "":
            return True

        compare = {}
        for i in range(len(s)):
            if s[i] not in compare:
                if t[i] in compare.values():
                    return False
                compare[s[i]] = t[i]
            else:
                if compare[s[i]] != t[i]:
                    return False

        return True

