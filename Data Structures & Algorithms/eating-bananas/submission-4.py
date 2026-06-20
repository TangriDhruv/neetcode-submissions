import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        max_pile = max(piles)
        rate = 1
        

        while low <= max_pile:
            mid = low + (max_pile -low)//2
            
            time = 0
            for j in piles:
                time = time + math.ceil(j/mid)
            if time <= h:
                rate = mid 
                max_pile = mid-1
                
            else:
                low = mid+1
                
        return rate
                



        