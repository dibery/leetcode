class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        split = len(costs) // 2
        for i in range(len(costs)):
            costs[i].insert(0, costs[i][0] - costs[i][1])
        return sum(cost[seq // split + 1] for seq, cost in enumerate(sorted(costs)))
