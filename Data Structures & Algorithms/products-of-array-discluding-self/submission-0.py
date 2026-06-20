class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        for i in range (0, len(nums)):
            temp = nums[i]
            total_right = 1
            for j in range (i+1,len(nums)): 
                if total_right == 1:
                    total_right = nums[j]
                else:
                    total_right = total_right * nums[j]
            right.append(total_right)
        left = []
        new_nums = nums[::-1]
        print(new_nums)
        for i in range (0, len(new_nums)):
            temp = new_nums[i]
            total_left = 1
            for j in range (i+1,len(new_nums)): 
                if total_left == 1:
                    total_left = new_nums[j]
                else:
                    total_left = total_left * new_nums[j]
            left.append(total_left)
        print(left)
        print(right)
        new_left = left[::-1]
        final_list = [x * y for x, y in zip(right, new_left)]

        return final_list
