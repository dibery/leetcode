import numpy
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums, L, H = numpy.array(nums), 1, sum(nums)
        while H - L > 5:
            M = (L + H) // 2
            if numpy.ceil(nums / M).sum() > threshold:
                L = M
            else:
                H = M
        for i in range(L, H + 1):
            if numpy.ceil(nums / i).sum() <= threshold:
                return i
