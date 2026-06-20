class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left = [1,1,2,8]
        #nums = [1,2,4,6]
        #right =[48,24,6,1]
        n = len(nums)
        left = [0]*n
        right = [0]*n
        ans = [0]*n
        left[0] = 1
        right[n-1] = 1
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        print(left)
        print(right)
        for i in range(0,n):
            ans[i] = left[i]*right[i]
        return ans



        