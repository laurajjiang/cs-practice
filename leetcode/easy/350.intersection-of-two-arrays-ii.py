#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        if len(nums2) > len(nums1):
            short_arr, long_arr = nums1, nums2
        short_arr, long_arr = nums2, nums1

        short_count = {}
        for num in short_arr:
            short_count[num] = short_count.get(num, 0) + 1

        for num in long_arr:
            if num in short_count:
                intersection.append(num)
                short_count[num] -= 1
                if short_count[num] == 0:
                    del short_count[num]
        return intersection


# @lc code=end

