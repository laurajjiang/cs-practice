#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = []
        s = set(A[0])

        for char in s:
            occurance = min([word.count(char) for word in A])
            if occurance > 0:
                common += [char] * occurance

        return common

