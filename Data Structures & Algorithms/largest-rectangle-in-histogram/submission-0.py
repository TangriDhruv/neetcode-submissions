class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        # For each bar as starting point
        for i in range(len(heights)):
            min_height = heights[i]
            
            # Extend rectangle from position i to the right
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                area = min_height * width
                max_area = max(max_area, area)
                
        return max_area