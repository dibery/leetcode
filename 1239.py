class Solution:
    def down(self, result, idx, arr):
        self.ans = max(self.ans, len(result))
        if idx == len(arr):
            return
        self.down(result, idx + 1, arr)
        result += arr[idx]
        if len(result) == len(set(result)):
            self.down(result, idx + 1, arr)

    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.down('', 0, arr)
        return self.ans
