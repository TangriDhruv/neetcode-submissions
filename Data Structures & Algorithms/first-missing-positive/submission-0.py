class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1,100000000000):
            if i not in nums:
                return i
        
        