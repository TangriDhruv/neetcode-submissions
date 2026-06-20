class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums) -1
        def dfs(index):

            if index >= n :
                return 0
            
            res = float("inf")
            for i in range(1, nums[index]+1):
                path = 1 + dfs(index+i)
                res = min(res,path)
            
            return res
        return dfs(0)
        