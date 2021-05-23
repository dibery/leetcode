class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n, s, ans = sorted(nums), sum(n), []
        while sum(ans) * 2 <= s:
            ans.append(n.pop())
        return ans
