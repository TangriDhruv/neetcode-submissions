class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mem = [0]*(len(cost)+1)
        def dfs(index):
            if index == 1 or index == 0:
                return 0
            if mem[index] != 0:
                return mem[index]
            mem[index] = min(dfs(index-1) + cost[index-1],dfs(index-2) + cost[index-2])
            return mem[index]
        
        return dfs(n)