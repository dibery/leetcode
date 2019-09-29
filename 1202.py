class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj = [set() for i in s]
        for i in pairs:
            adj[i[0]].add(i[1])
            adj[i[1]].add(i[0])
        proc = [False for i in s]
        s = list(s)
        for i in range(len(s)):
            if not proc[i]:
                reach, bfs = [i], [i]
                proc[i] = True
                while bfs:
                    f = bfs.pop(0)
                    for e in adj[f]:
                        if not proc[e]:
                            proc[e] = True
                            bfs.append(e)
                            reach.append(e)
                reach = sorted(reach)
                S = sorted(s[j] for j in reach)
                for j in range(len(reach)):
                    s[reach[j]] = S[j]
        return ''.join(s)
