class Solution:
    def dfs(self, idx, parent):
        self.ID += 1
        self.preorder[idx] = self.L[idx] = self.H[idx] = self.ID
        for i in self.adj[idx]:
            if self.preorder[i] == None:
                self.dfs(i, idx)
                self.ND[idx] += self.ND[i]
                self.L[idx] = min(self.L[idx], self.L[i])
                self.H[idx] = max(self.H[idx], self.H[i])
            elif i != parent:
                self.L[idx] = min(self.L[idx], self.preorder[i])
                self.H[idx] = max(self.H[idx], self.preorder[i])
    def check(self, idx):
        for i in self.adj[idx]:
            if self.preorder[idx] < self.preorder[i] and self.L[i] == self.preorder[i] and self.H[i] < self.preorder[i] + self.ND[i]:
                self.ans.append([idx, i])
    def criticalConnections(self, n: int, edge: List[List[int]]) -> List[List[int]]:
        self.preorder, self.L, self.H, self.ND, self.ID = [None] * n, [None] * n, [None] * n, [1] * n, 0
        self.adj, self.ans = [set() for i in range(n)], []
        for i in edge:
            self.adj[i[0]].add(i[1])
            self.adj[i[1]].add(i[0])
        self.dfs(0, 0)
        for i in range(n):
            self.check(i)
        return self.ans
