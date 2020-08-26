class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = nums[0]
        absMax = currMax

        for i in range(1, len(nums)):
            window = nums[i]
            currMax += window

            if window >= currMax:
                currMax = window
            absMax = max(absMax, currMax)
        return absMax

