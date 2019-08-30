#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        table = dict()
        for i in A:
            for j in B:
                sum = i + j
                if sum not in table:
                    table[sum] = 0
                table[sum] += 1

        count = 0
        for i in C:
            for j in D:
                sum = i + j
                if -sum in table:
                    count += table[-sum]
        return count

