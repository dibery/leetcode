class Solution:
    def topo(self, passive, active, n):
        proc, order = [False] * n, []
        for i in range(n):
            if not proc[i] and not passive[i]:
                proc[i], bfs = True, [i]
                order.append(i)
                while bfs:
                    f = bfs.pop(0)
                    for j in active[f]:
                        passive[j].remove(f)
                        if not passive[j]:
                            proc[j] = True
                            bfs.append(j)
                            order.append(j)
        return [] if len(order) < n else order

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group = [m + i if group[i] == -1 else group[i] for i in range(n)]
        grp_passive, grp_active = [[set() for i in range(m + n)] for i in '  ']
        idv_passive, idv_active = [[set() for i in range(n)] for i in '  ']
        grp_content, ans = [[] for i in range(m + n)], []
        for i in range(n):
            for j in beforeItems[i]:
                if group[j] != group[i]:
                    grp_passive[group[i]].add(group[j])
                    grp_active[group[j]].add(group[i])
                else:
                    idv_passive[i].add(j)
                    idv_active[j].add(i)
        for i in self.topo(idv_passive, idv_active, n):
            grp_content[group[i]].append(i)
        for i in self.topo(grp_passive, grp_active, m + n):
            ans += grp_content[i]
        return [] if len(ans) < n else ans
