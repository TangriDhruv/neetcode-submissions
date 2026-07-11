class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(0,n)}

        for edg,ver in edges:
            preMap[edg].append(ver)
            preMap[ver].append(edg)
        visiting = set()
        def dfs(edge,parent):
            if edge in visiting:
                return False
            visiting.add(edge)
            for pre in preMap[edge]:
                if pre == parent:
                    continue
                if not dfs(pre,edge):
                    return False
            return True
        
        
        return dfs(0,-1) and len(visiting) == n

        