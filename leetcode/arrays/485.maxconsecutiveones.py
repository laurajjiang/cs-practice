class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currMax = 0
        absMax = 0

        for num in nums:
            if num == 1:
                currMax += 1
            else:
                if currMax > absMax:
                    absMax = currMax
                currMax = 0

        return max(absMax, currMax)
