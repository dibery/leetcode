class Solution:
    def findSolution(self, f: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for i in range(1, 1001):
            for j in range(1, 1001):
                val = f.f(i, j)
                if val > z:
                    break
                if val == z:
                    ans.append([i, j])
        return ans
