class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index,prev):
            
            if index == len(nums):
                return 0
            if (index,prev) in memo:
                return memo[(index,prev)]
            #length = -1
            not_pick = dfs(index+1,prev)
            # when can i pick
            # if it's first element i.e. prev == -1 or nums[index] > nums[prev]
            pick = 0
            if (prev == -1 or nums[index]>nums[prev]):
                pick = 1+dfs(index+1,index)
                #length = max(not_pick,pick)
            memo[(index,prev)] = max(not_pick,pick)
            return memo[(index,prev)]
        return dfs(0,-1)

        
        