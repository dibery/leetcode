import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [i for i in itertools.combinations(range(1, 10), k) if sum(i) == n]
