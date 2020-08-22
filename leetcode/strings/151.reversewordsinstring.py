class Solution(object):
    def reverse(self, new, left, right): 
        while left < right:
            new[left], new[right] = new[right], new[left]
            left, right = left + 1, right - 1
        
    def reverse_word(self, new):
        length_ = len(new)
        start, end = 0, 0
        while start < length_:
            while end < length_ and new[end] != ' ':
                end += 1
            self.reverse(new, start, end-1)
            end += 1
            start = end
            
    def trim_whitespace(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        new = [] 
        while left <= right:
            if s[left] != ' ': 
                new.append(s[left])
            elif new[-1] != ' ':
                new.append(s[left])
            left += 1
        return new
            
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        trimmed = self.trim_whitespace(s)
        self.reverse(trimmed, 0, len(trimmed)-1)
        self.reverse_word(trimmed)
        return ''.join(trimmed)
        