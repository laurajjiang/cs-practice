class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = "" 
        for i in range(len(s)):
            tempRes = self.helper(s, i, i)
            if len(tempRes) > len(res):
                res = tempRes 
            tempRes = self.helper(s, i, i+1)
            if len(tempRes) > len(res):
                res = tempRes
        return res
    
    def helper(self, s, left, right): 
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left+1:right]
                