class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # adding the final top to the staircase.
        cost.append(0)
        #if the array is [1,2,3] and we added 0 then it becomes [1,2,3,0]
        # we are iterating in reverse
        #1. we know if we stand at 3 the only step we take is 1 and cost = 0 so no need to iterate that.
        #2. start from 2 that will be len(cost)-3
        # reverse for loop , start position, beigning of the array, decrement
        for i in range(len(cost)-3,-1,-1):
            cost[i]+= min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])