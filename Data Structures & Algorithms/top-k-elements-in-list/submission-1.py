class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num] = res[num] + 1
            else:
                res[num] = 1
        res1 = sorted(res.items(), key = lambda item: item[1], reverse= True)
        res = dict(res1)
        res_list = list(res.keys())
        return (res_list[:k])

