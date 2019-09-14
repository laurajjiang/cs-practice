#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        open_p = {"(", "[", "{"}
        pairs = {("(", ")"), ("[", "]"), ("{", "}")}
        stack = []
        for bracket in s:
            if bracket in open_p:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                recent_bracket = stack.pop()
                pair = (recent_bracket, bracket)
                if pair not in pairs:
                    return False
        if not stack:
            return True
        return False

