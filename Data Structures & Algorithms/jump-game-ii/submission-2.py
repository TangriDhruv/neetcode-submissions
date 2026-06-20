class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) -1
        memo = {}
        def dfs(index):

            if index >= n :
                return 0
            if index in memo:
                return memo[index]
            res = float("inf")
            for i in range(1, nums[index]+1):
                path = 1 + dfs(index+i)
                res = min(res,path)
            memo[index] = res
            
            return res
        return dfs(0)
        