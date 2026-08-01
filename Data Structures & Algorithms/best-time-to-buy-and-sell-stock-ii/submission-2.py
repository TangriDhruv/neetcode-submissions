
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if buy:
        # (-prices[index] + f(index,0),f(index+1,0)
        # (price[index]+min(f(index,1),f(index+1,1)),f(index+1,0))
        n= len(prices)
        dp = [[0]*2 for _ in range(0,len(prices)+1)]
        dp[n][0] = 0
        dp[n][1] = 0
        for i in range(n-1,-1,-1):
            dp[i][1] = max((-prices[i] + dp[i+1][0]),dp[i+1][1])
            dp[i][0] = max((prices[i] + dp[i+1][1]),dp[i+1][0])
        return dp[0][1]
        


        