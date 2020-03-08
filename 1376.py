class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = {i: [] for i in range(n)}
        for i in range(len(manager)):
            if manager[i] != -1:
                child[manager[i]].append(i)
        return self.time(child, informTime, headID)
    def time(self, child, informTime, head):
        return max(self.time(child, informTime, i) for i in child[head]) + informTime[head] if child[head] else 0
