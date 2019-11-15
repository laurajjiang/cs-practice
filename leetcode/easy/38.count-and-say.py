#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for j in range(1, n):
            curr = s[0]
            temp = ""
            count = 0
            for i in range(len(s)):
                if curr == s[i]:
                    count += 1
                else:
                    temp = temp + str(count) + curr
                    curr = s[i]
                    count = 1
                if i == len(s) - 1:
                    temp = temp + str(count) + curr
            s = temp
        return s


# @lc code=end

