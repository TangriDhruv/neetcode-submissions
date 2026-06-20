class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range (0,len(nums)):
            store[nums[i]] = i
        
        for i in range (0,len(nums)):
            comp = target - nums[i]
            if comp in store and store[comp] != i:
                return [i,store[comp]]
        return [] 
        