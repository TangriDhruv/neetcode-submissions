class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums)
        print(ub)
        

        for i in range (lb,ub):
            print("i:",i)
            print("lb",lb)
            print("ub",ub)
            mid = (lb + ub)/2
            print("mid",mid)
            if int(mid) > len(nums)-1:
                return -1
            elif target > nums[int(mid)]:
                lb = mid+1
            elif target < nums[int(mid)]:
                ub = mid-1
            else :
                return int(mid)
        return -1 
        