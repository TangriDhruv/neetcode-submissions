class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(day,buying):
            if day>=len(prices):
                return 0
            cooldown = dfs(day+1,buying)
            if buying:
                buy = dfs(day+1,not buying) - prices[day]
                return max(buy,cooldown)
            else:
                sell = dfs(day+2,not buying) + prices[day]
                return max(sell,cooldown)
        return dfs(0,True)
        
        