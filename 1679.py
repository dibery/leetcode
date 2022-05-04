from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = Counter(nums)
        return nums[k / 2] // 2 + sum(min(nums[i], nums[k - i]) for i in nums if i * 2 < k)
