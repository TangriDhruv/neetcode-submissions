class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brute
        dup = set()
        res = -1

        for i in range(0,len(nums)):
            if nums[i] in dup:
                res = nums[i]
                break
            dup.add(nums[i])
        
        return res
        