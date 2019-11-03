#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + costs[i - 1][0]
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + costs[i - 1][1]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(
                    dp[i - 1][j] + costs[i + j - 1][0],
                    dp[i][j - 1] + costs[i + j - 1][1],
                )
        return dp[-1][-1]


# @lc code=end

