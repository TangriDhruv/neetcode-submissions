class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        k = len(nums)-1

        while j<=k:
            if nums[j] == 1:
                j=j+1
            
            elif nums[j] == 0:
                temp= nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i = i+1
                j = j+1
            
            elif nums[j] == 2:
                temp= nums[k]
                nums[k] = nums[j]
                nums[j] = temp
                k = k-1
            
        return nums
        