class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        forth, back = [0], []
        for i in nums:
            forth[-1] += 1
            if i % 2:
                forth.append(0)
        for i in nums:
            if i % 2:
                back.append(1)
            elif back:
                back[-1] += 1
        return sum(forth[i] * back[i + k - 1] for i in range(len(forth) - k))
