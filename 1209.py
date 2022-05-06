class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cnt = [['', 0]]
        for i in s:
            if i != cnt[-1][0]:
                cnt.append([i, 1])
            else:
                cnt[-1][1] += 1
            if cnt[-1][1] == k:
                cnt.pop()
        return ''.join(i[0] * i[1] for i in cnt)
