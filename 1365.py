class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len(list(j for j in nums if j < i)) for i in nums]