class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            dict[num] = 1

        result = []
        for i in range(1, len(nums) + 1):
            if i not in dict:
                result.append(i)

        return result
