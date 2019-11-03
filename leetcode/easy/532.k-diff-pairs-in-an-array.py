#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        numsSet, pairsSet = set(), set()
        for num in nums:
            for pair in [num + k, num - k]:
                if pair in numsSet:
                    pairsSet.add(tuple(sorted([num, pair])))
                numsSet.add(num)
        return len(pairsSet)


# @lc code=end

