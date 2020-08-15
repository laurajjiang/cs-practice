class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")
        maxprofit = 0
        for num in prices:
            if num < minprice:
                minprice = num
            elif num - minprice > maxprofit:
                maxprofit = num - minprice
        return maxprofit
