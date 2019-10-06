class Solution:
    def arraysIntersection(self, a: List[int], b: List[int], c: List[int]) -> List[int]:
        return sorted(set(a) & set(b) & set(c))
