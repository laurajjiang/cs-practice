#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price, max_profit = max(prices), 0

        for stock in prices:
            min_price = min(min_price, stock)
            max_profit = max(max_profit, stock - min_price)
        return max_profit


# @lc code=end

