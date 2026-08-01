class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # lets try recursive approach
        # even if i can pick an interval i need to check if skipping it will lead to more number of intervals i can keep.
        # then calculate max number of intervals i can keep max(pick,not_pick)
        intervals.sort()
        dp = {}
        def dfs(index, prev):
            if index>= len(intervals):
                return 0
            if (index,prev) in dp:
                return dp[(index,prev)]
            pick = 0
            if prev == -1 or intervals[index][0]>=intervals[prev][1]:
                pick = 1 + dfs(index+1,index)
            notpick = dfs(index+1,prev)
            dp[(index,prev)] = max(pick,notpick)
            return dp[(index,prev)]
        return len(intervals) - dfs(0,-1)
        