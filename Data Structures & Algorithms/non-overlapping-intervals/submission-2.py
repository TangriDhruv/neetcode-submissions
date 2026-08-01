class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # lets try recursive approach
        intervals.sort()
        def dfs(index, prev):
            if index>= len(intervals):
                return 0
            pick = 0
            if prev == -1 or intervals[index][0]>=intervals[prev][1]:
                pick = 1 + dfs(index+1,index)
            notpick = dfs(index+1,prev)
            return max(pick,notpick)
        return len(intervals) - dfs(0,-1)
        