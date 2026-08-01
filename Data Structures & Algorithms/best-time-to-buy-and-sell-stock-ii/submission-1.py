class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if buy:
        # (-prices[index] + f(index,0),f(index+1,0)
        # (price[index]+min(f(index,1),f(index+1,1)),f(index+1,0))
        dp = {}
        def f(index,buy):
            if index >= len(prices):
                return 0
            if (index,buy) in dp:
                return dp[(index,buy)]
            if buy:
                dp[(index,buy)]=max((-prices[index] + f(index+1,0)),f(index+1,1))
            else:
                dp[(index,buy)] = max((prices[index] + f(index+1,1)),f(index+1,0))
            return dp[(index,buy)]
        return f(0,1)
        


        