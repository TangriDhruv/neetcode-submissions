class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+ count.get(num,0)
       # sort the dic in descending order
        print (count.items())
        count = sorted(count.items(), key = lambda item:item[1],reverse=True)
        print(count)
        count = dict(count)
        res = list(count.keys())
        return (res[:k]) 
        
