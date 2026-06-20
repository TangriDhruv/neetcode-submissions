from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            idx = bisect_left(tail,num)
            if idx == len(tail):
                tail.append(num)
            tail[idx] = num
        return len(tail)
        