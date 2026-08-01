class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def f(index,buy):
            if index >= len(prices):
                return 0
            if (index,buy) in dp:
                return dp[(index,buy)]
            if buy == 1:
                dp[(index,buy)] = max(-prices[index]+f(index+1,0), f(index+1,1))
                return dp[(index,buy)]
            else:
                dp[(index,buy)] = max(prices[index]+f(index+2,1),f(index+1,0))
                return dp[(index,buy)]
        return f(0,1)
        
        