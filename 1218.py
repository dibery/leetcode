class Solution:
    def longestSubsequence(self, num: List[int], diff: int) -> int:
        ans = {}
        for i in num:
            ans[i] = ans.get(i - diff, 0) + 1
        return max(ans.values())
