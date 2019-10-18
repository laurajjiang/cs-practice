#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        if not s:
            return ""
        for i in range(len(s)):
            palindrome = expansion(i, i)
            if len(palindrome) > len(res):
                res = palindrome
            palindrome = expansion(i, i + 1)
            if len(palindrome) > len(res):
                res = palindrome
        return res


# @lc code=end

