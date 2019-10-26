#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
                continue
            if i == len(flowerbed) - 1 or not flowerbed[i + 1]:
                n -= 1
                i += 2
            else:
                i += 1
        return n <= 0


# @lc code=end

