class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenNumDigits = 0

        for num in nums:
            digits = 0
            while num > 0:
                num = num / 10
                digits += 1
            if digits % 2 == 0:
                evenNumDigits += 1
        return evenNumDigits

