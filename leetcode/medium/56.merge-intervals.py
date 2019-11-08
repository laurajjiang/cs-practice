#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        l = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])
        l, r = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            cl, cr = intervals[i]
            if r < cl:
                res.append([l, r])
                l, r = cl, cr
            else:
                r = max(r, cr)
        res.append([l, r])
        return res


# @lc code=end

