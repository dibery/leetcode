class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for seq, c in enumerate(chalk):
            if k < c:
                return seq
            k -= c
