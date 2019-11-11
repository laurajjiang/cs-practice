#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring, length, max_len = "", 0, 0
        for char in s:
            if char in substring:
                index = substring.find(char)
                substring = substring[(index + 1) : :]
            substring += char
            length = len(substring)
            if length > max_len:
                max_len = length

        return max_len

