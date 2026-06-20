class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(index,total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (index,total) in memo:
                return memo[(index,total)]
            
            
            _sum_ = dfs(index+1, total + nums[index])
            _sub_ = dfs(index+1, total - nums[index])
            memo[(index,total)] =  _sum_ + _sub_
            return memo[(index,total)]
        return dfs(0,0)

        