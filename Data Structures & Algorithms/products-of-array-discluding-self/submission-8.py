class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        res = [1]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix_sum = prefix [i-1] * nums [i-1]
                prefix.append(prefix_sum)
        sufix = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                sufix[i] = 1
            else:
                sufix[i] = sufix[i+1]*nums[i+1]
        print(sufix)
        for i in range(0,len(nums)):
            res[i] =prefix[i]*sufix[i]
        
        return res


