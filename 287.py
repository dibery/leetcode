class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a, b = nums[nums[0]], nums[nums[nums[0]]]
        while a != b:
            a, b = nums[a], nums[nums[b]]
        a = nums[0]
        while a != b:
            a, b = nums[a], nums[b]
        return a
