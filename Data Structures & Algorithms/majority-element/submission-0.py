class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = len(nums) // 2
   
        res = 0
        max_element  = {}
        for i in range (0,len(nums)):
            max_element[nums[i]] = max_element.get(nums[i],0) + 1
        
        for i,j in max_element.items():


            if j > max_num:
                res = i
        
        return res
            

        