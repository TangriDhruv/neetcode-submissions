class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = defaultdict(list)
        for x,y in points:
            distance = math.sqrt((x*x - 0 + y*y - 0))
            stack[distance].append([x,y])
        
        stack = dict(sorted(stack.items()))
        
        
        res = []
        for key,val in (stack.items()):
    
            for v in val:
              
                if len(res) == k:
                    return res
                
                res.append(v)
        return res
            