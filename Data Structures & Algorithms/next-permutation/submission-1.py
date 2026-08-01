class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Find the break point index
        #the min value of the break point can be second last value starting from behind.
        # Break point is when when the next number is greater than current i.
        # For Ex: 215430 the break point is between 1 and 5.
        index = -1
        for i in range(len(nums)-2,-1,-1):
            print(nums[i])
            if nums[i] < nums[i+1]:
                print("((()))")
                index = i
                break

        print(index)
        # if we don't have a break point that means no next perutation exit and it would be the first permutation
        if index == -1:
            nums.reverse()
            return
        
        #once break point is found swap with the next big number

        for i in range(len(nums)-1,index,-1):
            print("hi",nums[i])
            if nums[i] > nums[index]:
                print("here")
                nums[index],nums[i] = nums[i],nums[index]
                break
        
        # reverse the order of number after the break point since they will be in desc order sorted.

        nums[index+1:]=reversed(nums[index+1:])
        
        

        




