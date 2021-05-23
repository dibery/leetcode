class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        try:
            a = b = nums.index(0)
            while b < len(nums):
                while nums[b] == 0:
                    b += 1
                nums[a], nums[b] = nums[b], nums[a]
                b += 1
                while nums[a]:
                    a += 1
        except:
            pass
