#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters) - 1
        while l < h:
            m = (l + h) // 2
            if letters[m] > target:
                h = m
            else:
                l = m + 1
        return letters[l] if letters[l] > target else letters[0]

