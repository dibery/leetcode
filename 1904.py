class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def conv(H, M):
            return H * 60 + M
        s = conv(*map(int, startTime.split(":")))
        f = conv(*map(int, finishTime.split(":")))
        if 0 <= f - s < 15:
            return 0
        s = (s + 15 * (s % 15 != 0) - s % 15) % 1440
        f -= f % 15
        return (f - s) // 15 if f >= s else 96 - (s - f) // 15
