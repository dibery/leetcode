import numpy

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return True if numpy.gcd.reduce(nums) == 1 else False
