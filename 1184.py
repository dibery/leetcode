class Solution:
    def distanceBetweenBusStops(self, D: List[int], S: int, T: int) -> int:
        s, S, T = sum(D), min(S, T), max(S, T)
        go = sum(D[S:T])
        return min(go, s - go)
