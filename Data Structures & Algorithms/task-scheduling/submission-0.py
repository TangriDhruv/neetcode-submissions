class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapping = {}
        time = 0
        for task in tasks:
            mapping[task] = mapping.get(task,0)+1
        #to create maxheap first create a normal list
        maxHeap = []
        for cnt in mapping.values():
            maxHeap.append(-cnt)
        #now heapify
        heapq.heapify(maxHeap)

        q = deque() #[cnt,idletime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
            



        