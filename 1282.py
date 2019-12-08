class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grp, ans = {}, []
        for i, size in enumerate(groupSizes):
            if size not in grp:
                grp[size] = []
            grp[size].append(i)
        for size in grp:
            for i in range(0, len(grp[size]), size):
                ans.append(grp[size][i:i + size])
        return ans
