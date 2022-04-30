class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        ans = []
        for e, v in zip(equations, values):
            adj.setdefault(e[0], {})[e[1]] = v
            adj.setdefault(e[1], {})[e[0]] = 1 / v
        def dfs(var, val, vis):
            for i in adj.get(var, {}):
                if i not in vis:
                    vis[i] = val * adj[var][i]
                    dfs(i, vis[i], vis)
        for s, t in queries:
            vis = {}
            dfs(s, 1, vis)
            ans.append(vis.get(t, -1.0))
        return ans
