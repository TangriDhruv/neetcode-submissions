class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i,num in enumerate(nums):
            print(i)
            print(num)
            if i != num:
                return i
        return len(nums)
        