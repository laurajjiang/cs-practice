#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = {}
        hash_t = {}
        for char in s:
            if char in hash_s:
                hash_s[char] += 1
            else:
                hash_s[char] = 1

        for char in t:
            if char in hash_t:
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        for char in t:
            if char not in hash_s:
                return char
            else:
                if hash_t[char] != hash_s[char]:
                    return char


# @lc code=end

