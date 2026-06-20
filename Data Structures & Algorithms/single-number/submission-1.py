class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range (0, len(nums)):
            xor = nums[i]^xor
        return xor
        