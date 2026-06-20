class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}#{3:0,4:1,5:2,6:3}

        for i,n in enumerate(nums):
            seen[n] = i
        print(seen)
        for i,n in enumerate(nums):
            comp = target - n
            print(comp) 
            if comp in seen and i != seen[comp]:
                return [i,seen[comp]]
        return []
        

        