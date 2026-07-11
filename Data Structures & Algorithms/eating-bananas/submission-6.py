class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        rate = 1

        while l <= r:
            mid = l +(r-l)//2
            time = 0
            for j in piles:
                time = time + math.ceil(j/mid)
            
            if time <= h:
                rate = mid
                r = mid - 1
            else:
                l = mid+1
        
        return rate
