#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in zip(*strs):
            # i is each individual letter, set doesn't care for repeats
            # so set(i) contains either a single letter or > 1

            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

