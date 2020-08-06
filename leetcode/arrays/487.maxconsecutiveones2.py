class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOnes = 0
        currMax = 0
        possibleMax = 0
        flipZero = False
        
        for num in nums:
            if num == 1:
                currMax += 1
                possibleMax += 1
            elif num == 0 and not flipZero:
                flipZero = True
                currMax = 0
                possibleMax += 1
            elif num == 0 and flipZero:
                maxOnes = max(possibleMax, maxOnes)
                possibleMax = currMax + 1
                currMax = 0
        return max(maxOnes, possibleMax)
        
        