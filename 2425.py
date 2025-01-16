from functools import reduce
from operator import xor

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return (0 if len(nums2) % 2 == 0 else reduce(xor, nums1)) ^ (0 if len(nums1) % 2 == 0 else reduce(xor, nums2))
