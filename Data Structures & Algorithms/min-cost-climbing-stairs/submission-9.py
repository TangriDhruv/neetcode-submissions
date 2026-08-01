class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        def dfs(index):
            if index == 0 or index == 1:
                return 0
            if index in cache:
                return cache[index]
            cache[index]=min(dfs(index-1) + cost[index-1],dfs(index-2) + cost[index-2])
            return cache[index]
        return dfs(n)
        