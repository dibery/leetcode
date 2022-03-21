class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cand = set((tops[0], bottoms[0]))
        for t, b in zip(tops, bottoms):
            cand &= set((t, b))
        if not cand:
            return -1
        cand = list(cand)
        return min(tops.count(cand[0]), len(tops) - tops.count(cand[0]), bottoms.count(cand[0]), len(tops) - bottoms.count(cand[0]))
