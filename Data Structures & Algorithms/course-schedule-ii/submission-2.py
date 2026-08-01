class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        res = []
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            res.append(crs)
            return True
        
        for cr in range(numCourses):
            if not dfs(cr):
                return []
        return res
        