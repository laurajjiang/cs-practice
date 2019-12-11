#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i]) + 1
            for j in range(idx, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res


# @lc code=end

