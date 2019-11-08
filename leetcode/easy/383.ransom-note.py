#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] not in magazine:
                return False
            magazine = magazine.replace(ransomNote[i], "", 1)
            i += 1
        return True


# @lc code=end

