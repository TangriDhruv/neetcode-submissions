class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l]>prices[r]:
                l = r
            else:
                max_prof = max(max_prof,prices[r]-prices[l])
            r = r+1
        return max_prof