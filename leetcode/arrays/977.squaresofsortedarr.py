class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = []
        for i in range(len(A)):
            sq = A[i] * A[i]
            squares.append(sq)

        squares.sort()
        return squares
