class Solution:
    def stoneGameIII(self, stone: List[int]) -> str:
        value = [(0, 0)]
        for i in range(len(stone))[::-1]:
            value.append(max((
                sum(stone[i:i + j]) + value[len(stone) - i - j][1], value[len(stone) - i - j][0]) 
                for j in range(1, 4) if i + j <= len(stone)))
        if value[-1][0] > value[-1][1]:
            return 'Alice'
        if value[-1][0] < value[-1][1]:
            return 'Bob'
        return 'Tie'
