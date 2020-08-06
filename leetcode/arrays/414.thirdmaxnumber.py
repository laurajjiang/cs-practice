class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = set()
        for num in nums:
            maximum.add(num)
            if len(maximum) > 3:
                maximum.remove(min(maximum))
        if len(maximum) < 3:
            return max(maximum)
        return min(maximum)
