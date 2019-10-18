#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        def expansion(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l += 1
                r += 1
            return count

        palindromes = 0
        for i in range(len(s)):
            palindromes += expansion(i, i)
            palindromes += expansion(i, i + 1)
        return palindromes


# @lc code=end

