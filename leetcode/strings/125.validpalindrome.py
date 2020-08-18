class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        lo, hi = 0, len(s) - 1

        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo] != s[hi] and lo < hi:
                return False
            lo += 1
            hi -= 1
        return True

