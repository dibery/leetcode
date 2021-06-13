class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        idx = [{} for i in range(3)]
        found = [False] * 3
        for seq, t in enumerate(triplets):
            for i in range(3):
                if t[i] == target[i] and all(x <= y for x, y in zip(t, target)):
                    found[i] = True
        return all(found)
