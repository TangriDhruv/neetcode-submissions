class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = len(prices)-1
        profit = 0
        # while l<r:
        #     profit = max(prices[r] - prices[l],profit)
        #     if (prices[l]>prices[r]):
        #         l= l+1
        #     else:
        #         r = r-1
        # return profit
        for i in range (0, len(prices)-1):
            for j in range (i+1, len(prices)):
                profit = max (profit,prices[j]-prices[i])
        return profit

        