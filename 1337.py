class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[1] for i in sorted((sum(m), seq) for seq, m in enumerate(mat))[:k]]
