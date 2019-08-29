#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = list(bin(N)[2:])
        for i in range(len(binary)):
            binary[i] = str(abs(int(binary[i]) - 1))
        return int("".join(binary), 2)

