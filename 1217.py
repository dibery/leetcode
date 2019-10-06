class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        return min(len([x for x in chips if x % 2 == 0]), len([x for x in chips if x % 2 == 1]))
