from itertools import product
from numpy import array
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        nums = array(nums)
        bit = [(nums & i == 0).sum() for i in range(2 ** 16)]
        return sum(bit[x & y] for x, y in product(nums, repeat=2))
