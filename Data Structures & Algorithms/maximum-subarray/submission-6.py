class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute
        if len(nums) == 1:
            return nums[0]
        max_sum = float("-inf")
        for i in range(0,len(nums)):
            total = nums[i]
            max_sum = max(max_sum,total)
            for j in range(i+1,len(nums)):
                total = total + nums[j]
                max_sum = max(max_sum,total)
        return max_sum
                
        