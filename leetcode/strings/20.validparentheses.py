class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        for i in range(len(s)): 
            if s[i] in '{[(': 
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                pair = stack.pop()
                if not self.isMatch(s[i], pair):
                    return False
        return len(stack) == 0
        
    def isMatch(self, curr, pair):
        openPar = ['(','{','[']
        closePar = [')','}',']']
        return openPar.index(pair) == closePar.index(curr)