#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        triplets = set()
        for i in range(l-2):
            a = nums[i]
            idx = set()
            for j in range(i+1, l):
                b = nums[j]
                c = -a-b
                if b not in idx:
                    idx.add(c)
                else:
                    triplets.add((a,b,c))
        return map(list, triplets)


# @lc code=end

