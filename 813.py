class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        ans = [[0] * (k + 1) for _ in range(len(nums))]
        ans[0] = [0] + [nums[0]] * k
        S = nums[0]
        for i in range(1, len(nums)):
            ans[i][1] = (ans[i - 1][1] * i + nums[i]) / (i + 1)
            S += nums[i]
            for j in range(2, k + 1):
                s = S
                ans[i][j] = ans[i][j - 1]
                for x in range(i):
                    s -= nums[x]
                    ans[i][j] = max(ans[i][j], ans[x][j - 1] + s / (i - x))
        return ans[-1][-1]
