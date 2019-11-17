class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            new = []
            for i in range(len(arr)):
                if i in [0, len(arr) - 1]:
                    new.append(arr[i])
                elif arr[i] > max(arr[i - 1], arr[i + 1]):
                    new.append(arr[i] - 1)
                elif arr[i] < min(arr[i - 1], arr[i + 1]):
                    new.append(arr[i] + 1)
                else:
                    new.append(arr[i])
            if new == arr:
                break
            arr = new
        return arr
