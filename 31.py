class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(-1, len(nums) - 1)[::-1]:
            if nums[i] < nums[i + 1]:
                break
        if i == -1:
            nums[::] = nums[::-1]
        else:
            pos = (1000, i)
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and nums[j] <= pos[0]:
                    pos = (nums[j], j)
            nums[i], nums[pos[1]] = nums[pos[1]], nums[i]
            nums[i + 1:] = nums[i + 1:][::-1]