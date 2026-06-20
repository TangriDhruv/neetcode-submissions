class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        print(len(seen))
        if len(seen) == len(nums):
            return False
        return True

        