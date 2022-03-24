class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        ans = 0
        b, e = 0, len(people) - 1
        while b <= e:
            if p[e] + p[b] <= limit:
                ans, e, b = ans + 1, e - 1, b + 1
            else:
                ans, e = ans + 1, e - 1
        return ans
