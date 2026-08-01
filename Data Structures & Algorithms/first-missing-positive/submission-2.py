class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        for i in range(0,len(nums)):
            if nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = 1
        #print(nums)

        for i in range(0, len(nums)):
            nums[abs(nums[i]) - 1] = -1*nums[abs(nums[i]) - 1] if nums[abs(nums[i]) - 1] >0 else nums[abs(nums[i]) - 1]
            #print(nums)

        for i in range(0,len(nums)):
            if nums[i] >0:
                return i+1
        return len(nums)+1


        