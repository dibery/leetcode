class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diff = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        m = min(diff)
        return [(arr[i], arr[i + 1]) for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == m]
