class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[i] + nums[-i - 1] for i in range(len(nums)))