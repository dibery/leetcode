import numpy
class Solution:
    def dfs(self, node, depth=0):
        self.vis[node], self.dist[node] = True, depth
        self.dist[node] = depth
        for i in self.adj[node]:
            if not self.vis[i]:
                self.dfs(i, depth + 1)
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.V = numpy.max(edges) + 1
        self.adj = [set() for i in range(self.V)]
        self.vis, self.dist = [False] * self.V, [0] * self.V
        for e in edges:
            self.adj[e[0]].add(e[1])
            self.adj[e[1]].add(e[0])
        self.dfs(0)
        self.vis = [False] * self.V
        self.dfs(numpy.argmax(self.dist), 0)
        return max(self.dist)
