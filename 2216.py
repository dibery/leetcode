class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ok = []
        for n in nums:
            if len(ok) % 2 == 1 and ok[-1] != n or len(ok) % 2 == 0:
                ok.append(n)
        return len(nums) - len(ok) + len(ok) % 2