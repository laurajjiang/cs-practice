#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

