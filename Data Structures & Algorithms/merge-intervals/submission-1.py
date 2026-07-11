class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        res = []
        intervals.sort()
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            print(stack)
            if intervals[i][0]<= stack[-1][1]:
                start,end = stack.pop()
                print("Start:",start)
                print("End:",end)
                end = max(end,intervals[i][1])
                stack.append([start,end])
            else:
                stack.append([intervals[i][0],intervals[i][1]])
        
        return stack

        