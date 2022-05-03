class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        small, large = [float('inf')], [float('-inf')]
        for n in nums:
            large.append(max(large[-1], n))
        for n in nums[::-1]:
            small.append(min(small[-1], n))
        large, small = large[:-1], small[-2::-1]
        start, end = 0, len(nums) - 1
        while start < len(nums) and nums[start] <= small[start]:
            start += 1
        while end >= start and nums[end] >= large[end]:
            end -= 1
        return max(0, end - start + 1)
