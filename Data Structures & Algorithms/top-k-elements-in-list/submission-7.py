class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(0,len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        freq =[[] for i in range(0,len(nums)+1)]
        
        for num,cnt in count.items():
            freq[cnt].append(num)
        print(freq)

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        