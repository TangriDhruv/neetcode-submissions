class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0

        while l < r:
            max_water = max(max_water,(r-l)*min(heights[l],heights[r]))
            if heights[l] > heights[r]:
                r = r-1
            elif heights[l] <= heights[r]:
                l = l+1
        
        return max_water
            
        