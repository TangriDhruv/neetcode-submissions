class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        print(n)
        def dfs(index):
            if index == 1 or index == 0:
                return 0
            return min(dfs(index-1) + cost[index-1],dfs(index-2) + cost[index-2])
        # def dfs1(index):
        #     if index == 0:
        #         return 0
        #     return min(dfs1(index-1) + cost[index-1],dfs1(index-2) + cost[index-2])
        return dfs(n)