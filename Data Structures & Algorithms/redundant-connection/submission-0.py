class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]  # path compression
                x = par[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # already connected -> redundant edge

            if rank[ra] < rank[rb]:
                par[ra] = rb
            elif rank[ra] > rank[rb]:
                par[rb] = ra
            else:
                par[rb] = ra
                rank[ra] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]