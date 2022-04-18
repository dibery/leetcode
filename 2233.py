import heapq, math
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            v = heapq.heappop(nums)
            heapq.heappush(nums, v + 1)
        ans = 1
        for i in nums:
            ans = ans * i % 1000000007
        return ans
