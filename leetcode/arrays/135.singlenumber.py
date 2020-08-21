class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen.keys(): 
                seen[num] += 1
            else: 
                seen[num] = 1
        
        for num in nums:
            if seen[num] == 1:
                return num
                
    # bit solution - use XOR (for num in nums, unique ^= num, return unique)