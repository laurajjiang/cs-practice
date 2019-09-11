#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count, i = 0, 5
        while (n // i) >= 1:
            count += int(n / i)
            i *= 5
        return count

        # return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

