class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index,l,total):
            if total == target:
                res.append(l[:])
                return
            if index>=len(nums) or total>target:
                return
            
            l.append(nums[index])
            backtrack(index,l,total+nums[index])
            l.pop()
            backtrack(index+1,l,total)
        backtrack(0,[],0)
        return res

        