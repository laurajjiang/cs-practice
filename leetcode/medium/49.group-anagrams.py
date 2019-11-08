#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for anagram in strs:
            s = ""
            for char in sorted(anagram):
                s += char
            if s not in anagrams:
                anagrams[s] = [anagram]
            else:
                anagrams[s].append(anagram)
        return list(anagrams.values())


# @lc code=end

