class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.ok = True
        vis = [False] * len(graph)
        def dfs(id, mark):
            if vis[id] != False or not self.ok:
                if vis[id] != mark:
                    self.ok = False
                return
            vis[id] = mark
            for i in graph[id]:
                dfs(i, ~mark)
        for i in range(len(graph)):
            if vis[i] is False:
                dfs(i, 0)
            if not self.ok:
                return False
        return True
