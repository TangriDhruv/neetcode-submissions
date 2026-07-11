class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            print(heights[l])
            print(heights[r])
            max_area = max(max_area,min(heights[l],heights[r])*(r-l))
            print(max_area)
            if heights[l]<=heights[r]:
                l = l+1
            else:
                r = r-1
        return max_area

        
        