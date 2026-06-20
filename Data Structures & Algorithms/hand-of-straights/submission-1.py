class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        #Create a count dict for storing the value and its frequency
        count = {}
        for i in hand:
            count[i] = 1+count.get(i,0)
        
        #Create a min heap to store the values (key in count). Min heap will give min value in O(1)
        minHeap = list(count.keys())
        #heapify
        heapq.heapify(minHeap)
        #Run the loop until heap has value
        while minHeap:
            first = minHeap[0]
            # run for loop to have consecutive set of group [1,2,3,4]
            for i in range(first,first+groupSize):
                if i not in count or count[i] == 0:
                    return False
                count[i] = count[i] - 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True