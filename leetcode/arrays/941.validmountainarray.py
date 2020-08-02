class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        length_ = len(A)

        while i + 1 < length_ and A[i] < A[i + 1]:
            i += 1

        if i == 0 or i == length_ - 1:
            return False

        while i + 1 < length_ and A[i] > A[i + 1]:
            i += 1

        return i == length_ - 1

