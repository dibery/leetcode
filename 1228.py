class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[1] < arr[0]:
            arr = arr[::-1]
        diff = max(set(arr[i] - arr[i - 1] for i in range(1, len(arr))))
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == diff:
                return arr[i] - diff // 2
