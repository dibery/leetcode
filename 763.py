class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        while s:
            end = s.rfind(s[0])
            idx = 0
            while idx <= end:
                end = max(end, s.rfind(s[idx]))
                idx += 1
            s = s[end + 1:]
            ans.append(end + 1)
        return ans
