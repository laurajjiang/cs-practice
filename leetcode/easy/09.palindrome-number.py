#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
#


class Solution:
    def isPalindrome(self, x):
        temp = str(x)[::-1]
        if "-" not in temp:
            temp = int(temp)
            if temp == x:
                return True
        return False

        # one line solutionn:
        # return str(x) == str(x)[::-1]

        # non-string solution:
        # all negative numbers will return false
        # while x != 0:
        # digit = x % 10           # Retrieves the last digit of number
        # reverse = reverse * 10 + rem     # Reverses the number
        # x = x // 10
        # if reverse == x:
        # return true

