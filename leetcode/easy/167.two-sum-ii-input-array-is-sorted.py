#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum > target:
                high -= 1
            elif sum == target:
                return [low + 1, high + 1]
            else:
                low += 1

