class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index,current,total):
            if total == target:
                result.append(current[:])
                return
            elif total > target:
                return
            else:
                for i in range(index,len(nums)):
                    current.append(nums[i])
                    backtrack(i,current,total + nums[i])
                    current.pop()
                
        backtrack(0,[],0)
        return result

        