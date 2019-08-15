#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_a = 0
        num_b = 0
        stack = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_a += 1
            else:
                if secret[i] not in stack:
                    stack[secret[i]] = 0

                if stack[secret[i]] < 0:
                    num_b += 1
                    stack[secret[i]] += 1

                if guess[i] not in stack:
                    stack[guess[i]] = 0

                if stack[guess[i]] > 0:
                    num_b += 1

                stack[guess[i]] -= 1
        return str(num_a) + "A" + str(num_b) + "B"

