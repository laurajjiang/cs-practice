#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        s, l = [], len(nums)
        for i, n in enumerate(nums):
            if i in s:
                continue
            d = []
            while n * nums[i] > 0:
                if i in d:
                    if d[-1] != i:
                        return True
                    else:
                        break
                d.append(i)
                s.append(i)
                i = (i + nums[i]) % l
        return False


# @lc code=end

