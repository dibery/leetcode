class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for i in nums:
            if not lis or i > lis[-1]:
                lis.append(i)
            else:
                for j in range(len(lis)):
                    if i <= lis[j]:
                        lis[j] = i
                        break
            if len(lis) >= 3:
                return True
        return False
