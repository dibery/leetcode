class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = score = 0
        for i in s:
            score += 1 if i == 'L' else -1
            if score == 0:
                ans += 1
        return ans
