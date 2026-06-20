class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(index,l):
            if index == len(nums):
                res.append(l[:])
                return
            if index > len(nums):
                return
            l.append(nums[index])
            backtrack(index+1,l)
            l.pop()
            while index+1 <len(nums) and nums[index] == nums[index+1]:
                index = index+1
            backtrack(index+1,l)
        
        backtrack(0,[])
        
        return res
        