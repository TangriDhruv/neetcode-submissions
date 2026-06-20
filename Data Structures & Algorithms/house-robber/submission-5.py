class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        
        dp =[-1]*len(nums)
        # so in dp below are the base cases if you can get them.
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])

        for i in range(2,len(nums)):
            #1. if we choose first element then the third element  = first + third
            #2. if we choose second element then fourth element = max(dp[3],dp[2]+nums)
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        print
        return dp[-1]