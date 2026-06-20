class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index,total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            
            _sum_ = dfs(index+1, total + nums[index])
            _sub_ = dfs(index+1, total - nums[index])
            return _sum_ + _sub_
        return dfs(0,0)

        