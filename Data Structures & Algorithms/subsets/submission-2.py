class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result =[]

        def backtrack(index, current):
            if index == len(nums):
                # create a copy of current because when you add list to list it stores the reference of list.
                # Hence if we don't append as a copy only the end state gets stored.
                result.append(current[:])
                return
            else:
                current.append(nums[index])
                backtrack(index+1,current)
                # empty the stack to find new paths.
                current.pop()
                backtrack(index+1,current)
                
        
        backtrack(0,[])
        return result

























        