class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count, last = [[0], [0]], None
        for i in s:
            if i != last:
                last = i
                count[int(i)].append(0)
            count[int(i)][-1] += 1
        return max(count[1]) > max(count[0])