class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index,l,total):
            if total == target:
                res.append(l[:])
                return
            if index>=len(candidates) or total>target:
                return
            l.append(candidates[index])
            backtrack(index+1,l,total+candidates[index])
            l.pop()
            while index+1<len(candidates) and candidates[index] == candidates[index+1]:
                index = index+1
            backtrack(index+1,l,total)
        
        backtrack(0,[],0)
        return res

        