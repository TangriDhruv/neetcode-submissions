class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        nums.sort()
        for i in range (0,len(nums)):
            print("here")
            for j in range (i+1,len(nums)):
                print("here")
                for k in range (j+1,len(nums)):
                    print("here")
                    if(nums[i]+nums[j]+nums[k] == 0):
                        tmp =[nums[i],nums[j],nums[k]]
                        s.add(tuple(tmp))
        return [list(i) for i in s]

        