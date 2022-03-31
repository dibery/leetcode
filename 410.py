class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, h = max(nums), sum(nums)
        while l < h:
            t = (l + h) // 2
            seg = [0]
            for n in nums:
                if seg[-1] + n <= t:
                    seg[-1] += n
                elif len(seg) <= m:
                    seg.append(n)
                else:
                    break
            if len(seg) > m:
                l = t + 1
            else:
                h = t
        return l
