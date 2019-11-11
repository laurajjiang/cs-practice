#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0:
        while i < n:
            num = data[i]
            n_byte = 0
            mask = 1 << 7 
            while mask & num: 
                n_byte += 1
                mask = mask >> 1
            
            if n_byte == 0: 
                i += 1
                continue 

            if n_byte == 1 or n_byte > 4:
                return False

            n_byte -= 1

            if n_byte > (n-i-1):
                return False
            
            i += 1
            mask1 = 1 << 7
            mask2 = 1 << 6
            while n_byte > 0:
                if not (data[i] & mask1 and not (data[i] & mask2)):
                    return False
                i += 1
                n_byte -= 1
        return True

            

            

# @lc code=end

