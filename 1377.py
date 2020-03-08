class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        adj = {i: [] for i in range(n + 1)}
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        return self.p(t, 1, target, adj)
    def p(self, time, start, goal, adj, cp = 1, parent = None):
        if time == 0 or len(adj[start]) == 1 and parent is not None or len(adj[start]) == 0:
            return cp if start == goal else 0
        return max(self.p(time - 1, i, goal, adj, cp / (len(adj[start]) - (1 if parent else 0)), start) for i in adj[start] if i != parent)
