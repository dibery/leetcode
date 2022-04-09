from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        return sorted(nums.keys(), key=lambda i: nums[i])[-k:]
