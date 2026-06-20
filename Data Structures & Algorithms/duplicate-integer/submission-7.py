class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in range(0, len(nums)):
            result.add(nums[i])
        
        if len(result) == len(nums):
            return False
        return True
        