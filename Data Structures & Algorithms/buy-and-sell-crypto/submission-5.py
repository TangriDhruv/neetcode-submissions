class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r<= len(prices)-1:
            if prices[l] < prices[r]:
                maxP = max(maxP,prices[r]-prices[l])
            else:
                l = r
            r = r+1
        
        return maxP