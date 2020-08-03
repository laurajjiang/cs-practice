class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        evens = []
        odds = []
        for num in A:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        return evens + odds
            