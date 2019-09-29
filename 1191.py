class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        double, trible = arr * 2, arr * 3
        def kadane(A):
            s = ans = 0
            for i in A:
                s += i
                ans = max(ans, s)
                s = 0 if s < 0 else s
            return ans
        m, d, t = kadane(arr), kadane(double), kadane(trible)
        return max(m, d, d + (t - d) * (k - 2)) % 1000000007
