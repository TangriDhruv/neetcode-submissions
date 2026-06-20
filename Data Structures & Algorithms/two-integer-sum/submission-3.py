class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}

        for i in range(0,len(nums)):
            seen_map[nums[i]] = i
        
        for i in range(0,len(nums)):
            comp = target - nums[i]

            if comp in seen_map and seen_map[comp] != i :
                return [i,seen_map[comp]]
        return []
        