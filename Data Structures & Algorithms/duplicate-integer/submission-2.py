class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(type(nums))
        nums1 = sorted(nums)
        nums = nums1
        if (len(nums) == 0) :
            return False
        temp = nums[0]
        for i in range (1, len(nums)):
            if nums[i] == temp :
                return True
            else:
                temp = nums[i]
        return False

         