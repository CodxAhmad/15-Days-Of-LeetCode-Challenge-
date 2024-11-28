class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            elif prices[i]-mini>profit:
                profit = prices[i]-mini
        return profit
        