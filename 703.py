import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.n = k, sorted(nums)[-k:]
        heapq.heapify(self.n)

    def add(self, val: int) -> int:
        if len(self.n) == self.k:
            heapq.heappushpop(self.n, val)
        else:
            heapq.heappush(self.n, val)
        return self.n[0]
