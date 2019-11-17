class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        mod = [sorted([e for e in nums if e % 3 == i]) for i in range(3)]
        if s % 3 == 0:
            return s
        elif s % 3 == 1:
            A = B = 0
            if mod[1]:
                A = s - mod[1][0]
            if len(mod[2]) > 1:
                B = s - sum(mod[2][:2])
            return max(A, B)
        else:
            A = B = 0
            if mod[2]:
                A = s - mod[2][0]
            if len(mod[1]) > 1:
                B = s - sum(mod[1][:2])
            return max(A, B)
        return 0
