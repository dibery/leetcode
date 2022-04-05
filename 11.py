class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = sorted(((b, a) for a, b in enumerate(height)), reverse=True)
        l, r = min(h[0][1], h[1][1]), max(h[0][1], h[1][1])
        ans = min(h[0][0], h[1][0]) * (r - l)
        for water, pos in h[2:]:
            l, r = min(l, pos), max(r, pos)
            ans = max(ans, water * (r - l))
        return ans
