class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            *stones, y, x = sorted(stones)
            if x != y:
                stones.append(x - y)
        return sum(stones)
