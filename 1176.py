class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pt, s, i = 0, sum(calories[:k]), 0
        while k <= len(calories):
            if s > upper:
                pt += 1
            elif s < lower:
                pt -= 1
            if k == len(calories):
                break
            s += calories[k]
            s -= calories[i]
            k += 1
            i += 1
        return pt
