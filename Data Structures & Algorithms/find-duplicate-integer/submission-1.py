class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow =0
        fast =0

        while True:
            slow = nums[slow]
            print("slow",slow)
            fast = nums[nums[fast]]
            print("fast",fast)
            if slow == fast:
                break
        
        slow2 =0

        while True:
            slow2 = nums[slow2]
            print("slow2",slow2)
            slow = nums[slow]
            print("slow_again",slow)

            if slow == slow2:
                return slow
        
        
        