class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        cum, ans, s = [], [0] * len(stones), 0
        for i in stones:
            s += i
            cum.append(s)
        ans[-2] = cum[-1]
        for i in range(len(stones))[-3::-1]:
            ans[i] = max(ans[i + 1], cum[i] + stones[i + 1] - ans[i + 1])
        return ans[0]