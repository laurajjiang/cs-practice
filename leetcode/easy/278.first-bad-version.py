#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m - 1) == False and isBadVersion(m) == True:
                return m
            else:
                if isBadVersion(m) == False:
                    l = m + 1
                else:
                    r = m - 1
        return -1

