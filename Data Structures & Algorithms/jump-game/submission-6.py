class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #recursion:
        def dfs(index):
            
            if index == len(nums)-1:
                return True
            elif index >= len(nums):
                return False
            elif nums[index] == 0:
                return False
            
            for i in range(1,nums[index]+1):
                if dfs(index + i):
                    return True
            return False
        return dfs(0)

        
        

        