class Solution(object):
    def reverse(self, s, left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        
    def reverseIndividualWords(self, s):
        length_ = len(s)
        start, end = 0, 0
        
        while start < length_: 
            while end < length_ and s[end] != ' ':
                end += 1
            self.reverse(s, start, end-1)
            start = end + 1
            end += 1
        
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s)-1)
        self.reverseIndividualWords(s)
        
        
                