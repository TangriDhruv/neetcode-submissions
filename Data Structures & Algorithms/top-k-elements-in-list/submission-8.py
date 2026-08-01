class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        max_Heap = []
        for key,val in dic.items():
            heapq.heappush(max_Heap,(-val,key))
        #print(max_Heap)
        res = []
        for i in range(0,k):
            res.append(heapq.heappop(max_Heap)[1])
        return res



        