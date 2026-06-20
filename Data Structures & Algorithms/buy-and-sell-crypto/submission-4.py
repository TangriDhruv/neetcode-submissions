class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        r = 1
        max_P = 0

        while r<len(prices):
            if prices[l]<prices[r]:
                max_P  = max(max_P, prices[r]- prices[l])
            else:
                l = r
            r = r+1
        
        return max_P
        