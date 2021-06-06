from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum(seq * c[n] for seq, n in enumerate(sorted(set(nums))))
