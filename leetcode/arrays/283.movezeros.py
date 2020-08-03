class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        numZeros = 0
        while j < len(nums): 
            if nums[j] != 0: 
                nums[i] = nums[j]
                i += 1
            else:
                numZeros += 1
            j += 1
            
        for i in range(j - numZeros, len(nums)):
            nums[i] = 0
        return nums
            
            