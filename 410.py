class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, h = max(nums), sum(nums)
        while l < h:
            t = (l + h) // 2
            seg, _sum = 1, 0
            for n in nums:
                if _sum + n <= t:
                    _sum += n
                else:
                    seg, _sum = seg + 1, n
                if seg > m:
                    l = t + 1
                    break
            if seg <= m:
                h = t
        return l
