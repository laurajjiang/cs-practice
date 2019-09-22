#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        if A[0] > A[1]:
            return False
        """
		First loop's purpose is to find the peak and index of the peak
		"""
        peak = 0
        index = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                peak = A[i]
                index = i
                break
            # rule is that no number can't be equal
            if A[i] == A[i + 1]:
                return False

        for i in range(index + 1, len(A) - 1):
            if A[i] <= A[i + 1] or A[i] > peak:
                return False

        return True

