#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return self.isMonoInc(A) or self.isMonoDec(A)

    def isMonoInc(self, A: List[int]) -> bool:
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return False
        return True

    def isMonoDec(self, A: List[int]) -> bool:
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                return False
        return True


# @lc code=end

