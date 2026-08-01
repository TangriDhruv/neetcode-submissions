class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boat = 0
        #[1,2,4,5]
        
        while l <= r:
            print(people[l] + people[r]) #1. 6, #2. 6
            if people[l] + people[r] <= limit:
                l = l+1 #l = 1,2
            r = r-1 #r = 2,1 condition break
            boat = boat+1
        
        return boat
