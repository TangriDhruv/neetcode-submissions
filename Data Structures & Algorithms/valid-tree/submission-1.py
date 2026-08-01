class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(0,n)}

        for n1,n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        visited = set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)

            for n in preMap[node]:
                if n == parent:
                    continue
                if not dfs(n,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n
                
        