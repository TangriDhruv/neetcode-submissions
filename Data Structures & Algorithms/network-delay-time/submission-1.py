class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        preMap = {i:[] for i in range(1,n+1)}

        for n1,n2,w in times:
            preMap[n1].append((w,n2))
        
        minHeap = [(0,k)]
        t= 0
        visited = set()

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1
            for w2,n2 in preMap[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(visited) == n else -1

        