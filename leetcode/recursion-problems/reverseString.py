'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
'''

class Solution:
    def reverseString(self, s, lo=0, hi=None):
        if len(s) <= 1: 
            return s
        if hi == None:
            hi = len(s) - 1
        if lo > hi: 
            return
        char = s[lo]
        s[lo] = s[hi]
        s[hi] = char

        return self.reverseString(s, lo+1, hi-1)
        
