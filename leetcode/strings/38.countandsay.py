class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for _ in range(n-1): 
            letter, temp, count = res[0], '', 0
            for char in res: 
                if char == letter:
                    count += 1
                else: 
                    temp += str(count) + letter
                    letter = char
                    count = 1
            temp += str(count) + letter
            res = temp
        return res