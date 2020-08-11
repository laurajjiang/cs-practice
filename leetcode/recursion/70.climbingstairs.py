class Solution(object):
    def climbStairs(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        dp = [[0] for _ in range(N + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N]

