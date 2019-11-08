#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        l = list()
        dict_b = {"}": "{", ")": "(", "]": "["}
        open_b = dict_b.values()
        for bracket in s:
            if bracket in open_b:
                l.append(bracket)
            else:
                if len(l) > 0 and l[-1] == dict_b[bracket]:
                    l.pop()
                else:
                    return False
        return len(l) == 0

