class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        maxLength = 1
        unique = set()
        unique.add(s[0])
        start, end = 0, 1
        while start < len(s) and end < len(s):
            if s[end] in unique:
                unique.remove(s[start])
                start += 1
            else:
                unique.add(s[end])
                end += 1
                maxLength = max(maxLength, end - start)

        return maxLength
