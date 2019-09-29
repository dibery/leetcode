class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if all(x <= 0 for x in arr):
            return max(arr)
        neg, l = 0, len(arr)
        ans = [[max(0, arr[0])] * l for i in '**']
        for i in range(1, l):
            ans[0][i] = max(0, ans[0][i - 1] + arr[i])
            if arr[i] >= 0:
                ans[1][i] = ans[1][i - 1] + arr[i]
            else:
                if neg == 0:
                    ans[1][i], neg = ans[1][i - 1], arr[i]
                elif ans[0][i - 1] - ans[1][i - 1] >= arr[i]:
                    ans[1][i], neg = ans[0][i - 1], arr[i]
                else:
                    ans[1][i] = ans[1][i - 1] + arr[i]
                if ans[1][i] <= 0:
                    ans[1][i] = neg = 0
        return max(max(ans[0]), max(ans[1]))
