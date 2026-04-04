class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res

