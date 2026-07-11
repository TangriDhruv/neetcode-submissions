class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        def backtrack(index,l):
            if index == len(nums):
                res.append(l[:])
                return
            l.append(nums[index])
            backtrack(index+1,l)
            l.pop()
            backtrack(index+1,l)
        backtrack(0,[])
        return res


        