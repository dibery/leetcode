class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        M = ans = 0
        for i in range(len(light)):
            M = max(M, light[i])
            ans += 1 if M == i + 1 else 0
        return ans
