class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        left = nums[:len(nums)-1]
        right = nums[1:]

        dp_left = [-1] * len(left)
        dp_right =[-1] * len(right)

        dp_left[0] = left[0]
        dp_left[1] = max(dp_left[0],left[1])

        for i in range(2,len(left)):
            dp_left[i] = max(dp_left[i-1],left[i]+dp_left[i-2])
        
        dp_right[0] = right[0]
        dp_right[1] = max(dp_right[0],right[1])

        for i in range(2,len(right)):
            dp_right[i] = max(dp_right[i-1],right[i]+dp_right[i-2])
        
        return max(dp_left[-1],dp_right[-1])
        


        