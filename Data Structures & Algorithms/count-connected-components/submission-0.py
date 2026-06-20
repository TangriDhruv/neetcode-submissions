class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = {i:[] for i in range(0,n)}

        for i,j in edges:
            map[i].append(j)
            map[j].append(i)
        
        print(map)

        visited = set()
        count = 0

        def dfs(comp):
            for i in map[comp]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)

        for i in range(0,n):
            if i not in visited:
                visited.add(i)
                count = count+1
                dfs(i)
        return count