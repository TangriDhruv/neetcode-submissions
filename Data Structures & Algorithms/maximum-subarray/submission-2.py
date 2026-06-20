class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum = nums[0]
        max_sum = nums[0]

        # Iterate through the rest
        for i in range(1, len(nums)):
            # Either extend the previous subarray OR start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

        