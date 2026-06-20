class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        #res = [1,1,2,8]
        prev =1
        for i in range(1, len(nums)):
            prev = prev *nums[i-1]
            res[i] = prev
        post = 1
        for i in range(len(nums)-1,-1,-1):
            print(i)
            res[i] = res[i] * post
            post = post*nums[i]
        
        return res
        

        