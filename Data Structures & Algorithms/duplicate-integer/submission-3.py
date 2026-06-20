class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l =set(nums)
        print(type(l))
        print(nums)
        if len(nums) == len(l):
            return False 
        else:
            return True
        