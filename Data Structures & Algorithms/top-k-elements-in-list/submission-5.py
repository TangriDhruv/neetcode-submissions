class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for _ in range(0,len(nums)+1)]

        for i,n in enumerate(nums):
            seen[n] = seen.get(n,0)+1
        for num,cnt in seen.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
            
        