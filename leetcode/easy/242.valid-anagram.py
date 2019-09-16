#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1

        for char in t:
            if char not in t_map:
                t_map[char] = 1
            else:
                t_map[char] += 1

        return s_map == t_map

